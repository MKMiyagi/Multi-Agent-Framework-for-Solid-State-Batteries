import pickle
import json
import re
import torch
import operator
import os
from typing import TypedDict, List, Dict, Annotated, Literal, Any, Optional
from langgraph.graph import StateGraph, END
from huggingface_hub import InferenceClient
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.schema import NodeWithScore
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.embeddings.huggingface_api import HuggingFaceInferenceAPIEmbedding
from llama_index.postprocessor.flag_embedding_reranker import FlagEmbeddingReranker
from mp_api.client import MPRester

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Acceleration Device: {DEVICE.upper()}")

HF_API_KEY = os.getenv("HF_API_KEY")
MP_API_KEY = os.getenv("MP_API_KEY")
if not HF_API_KEY:
    raise ValueError("HF_API_KEY environment variable not set. Please export HF_API_KEY='your_key_here'")
if not MP_API_KEY:
    raise ValueError("MP_API_KEY environment variable not set. Please export MP_API_KEY='your_key_here'")

LLM_MODEL = "deepseek-ai/DeepSeek-V3.2-Exp"
EMBED_MODEL_NAME = "Qwen/Qwen3-Embedding-8B"

hf_client = InferenceClient(api_key=HF_API_KEY)

print("Initializing Embedding Models...")
embed_model = HuggingFaceInferenceAPIEmbedding(
    model_name=EMBED_MODEL_NAME, 
    token=HF_API_KEY
)
Settings.embed_model = embed_model

reranker = FlagEmbeddingReranker(
    model="BAAI/bge-reranker-v2-m3",
    top_n=15, 
    use_fp16=True
)

DEFAULT_MP_FIELDS = [
    "material_id",
    "formula_pretty",
    "energy_above_hull",
    "is_stable",
    "band_gap",
    "density",
    "volume",
    "nsites",
    "symmetry" 
]

def call_llm(prompt: str, max_tokens: int = 1000, temperature: float = 0.3) -> str:
    """Wrapper for DeepSeek LLM calls via Hugging Face"""
    try:
        response = hf_client.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"LLM Error: {e}")
        return f"ERROR: LLM call failed - {str(e)}"

def _get_rester() -> MPRester:
    return MPRester(MP_API_KEY)

def summarize_material_dict(mat: dict) -> str:
    formula = mat.get("formula_pretty", "N/A")
    e_hull = mat.get("energy_above_hull", "N/A")
    band_gap = mat.get("band_gap", "N/A")
    density = mat.get("density", "N/A")
    
    crystal = "N/A"
    if "symmetry" in mat and isinstance(mat["symmetry"], dict):
        crystal = mat["symmetry"].get("crystal_system", "N/A")
        
    return f"- {formula} ({crystal}): E_hull={e_hull} eV/atom, BandGap={band_gap} eV, Density={density} g/cc"

NL_QUERY_SYSTEM = """You are a JSON generator for Materials Project search.
Output ONLY valid JSON. 
Keys: elements, exclude_elements, chemsys, formula, is_stable, band_gap, energy_above_hull, limit=10.
Interpret "stable" as is_stable: true. "Metastable" as energy_above_hull: [0.01, 0.1]."""

def parse_nl_to_mp_query(nl_query: str) -> Dict[str, Any]:
    content = call_llm(f"{NL_QUERY_SYSTEM}\nQuery: {nl_query}", max_tokens=200, temperature=0.0)
    try:
        text = content.strip().strip("`").replace("json", "").strip()
        return json.loads(text)
    except: return {}

def search_materials_from_nl(nl_query: str) -> List[Dict[str, Any]]:
    spec = parse_nl_to_mp_query(nl_query)
    if not spec: return []

    search_kwargs = {k: v for k, v in spec.items() if v is not None and k != "limit"}
    
    if "band_gap" in search_kwargs: search_kwargs["band_gap"] = tuple(search_kwargs["band_gap"])
    if "energy_above_hull" in search_kwargs: search_kwargs["energy_above_hull"] = tuple(search_kwargs["energy_above_hull"])
    search_kwargs["fields"] = DEFAULT_MP_FIELDS

    try:
        with _get_rester() as mpr:
            docs = mpr.materials.summary.search(**search_kwargs)
            docs = docs[:spec.get("limit", 10)]
            out = []
            for d in docs:
                if hasattr(d, "dict"):
                    out.append(d.dict())
                else:
                    out.append({k: getattr(d, k, "N/A") for k in DEFAULT_MP_FIELDS})
            return out
    except Exception as e:
        print(f"MP API Error: {e}")
        return []

class ResearchState(TypedDict):
    query: str
    research_goal: str
    physical_constraints: str 
    retrieved_chunks: List[NodeWithScore]
    relevant_papers: List[Dict]
    literature_summary: str
    mp_summary_text: str 
    identified_mechanisms: List[Dict]
    patterns: str
    proposed_hypotheses: List[Dict]
    critic_score: float
    critic_feedback: str
    needs_revision: bool
    revision_suggestions: List[str]
    experimental_designs: List[Dict]
    recommended_next_steps: str
    iteration: int
    max_iterations: int
    execution_log: Annotated[List[str], operator.add]

print("\nLoading RAG index...")
try:
    with open("contextual_nodes.pkl", "rb") as f:
        all_nodes = pickle.load(f)
    print(f"Loaded {len(all_nodes)} nodes")

    vector_index = VectorStoreIndex(all_nodes, show_progress=False)
    vector_retriever = VectorIndexRetriever(index=vector_index, similarity_top_k=60)
    bm25_retriever = BM25Retriever.from_defaults(nodes=all_nodes, similarity_top_k=60)
    print("Retrievers ready")
except FileNotFoundError:
    print("'contextual_nodes.pkl' not found. Please run ingestion first.")
    all_nodes = [] 

def hybrid_retrieve(query: str, top_k: int = 15, use_reranker: bool = True) -> List[NodeWithScore]:
    if not all_nodes: return []
    initial_k = 50 if use_reranker else top_k 

    vector_results = vector_retriever.retrieve(query)
    bm25_results = bm25_retriever.retrieve(query)

    node_scores = {}
    for i, res in enumerate(vector_results):
        node_scores[res.node.node_id] = {'node': res.node, 'score': 0.5 / (60 + i)}
    
    for i, res in enumerate(bm25_results):
        if res.node.node_id in node_scores:
            node_scores[res.node.node_id]['score'] += 0.5 / (60 + i)
        else:
            node_scores[res.node.node_id] = {'node': res.node, 'score': 0.5 / (60 + i)}
    
    candidates = sorted(node_scores.values(), key=lambda x: x['score'], reverse=True)[:initial_k]
    nodes = [NodeWithScore(node=i['node'], score=i['score']) for i in candidates]

    if use_reranker:
        try:
            nodes = reranker.postprocess_nodes(nodes=nodes, query_str=query)
        except Exception as e:
            print(f"Reranker skipped: {e}")
            
    return nodes[:top_k]

def literature_analysis_agent(state: ResearchState) -> ResearchState:
    print("AGENT 1: LITERATURE ANALYSIS")
    
    query = state['query']
    print(f"Query: '{query}'")

    print("Expanding query...")
    expansion_prompt = f"""Generate 4 diverse search queries for: "{query}"
    Focus on Synonyms, Specific Materials, and Mechanisms. Optimize queries for RAG.
    Return ONLY the list of 4 queries. No conversational text."""
    
    raw_text = call_llm(expansion_prompt, max_tokens=200, temperature=0.3)

    clean_text = re.sub(r'<think>.*?</think>', '', raw_text, flags=re.DOTALL)
    lines = [l.strip() for l in clean_text.split('\n') if l.strip()]
    variations = []
    for line in lines[:10]:
        clean = re.sub(r'^[\d\-\.\)\s"]+', '', line).strip('"\'')
        if len(clean) > 5 and '?' not in clean:
            variations.append(clean)
    
    search_queries = [query] + variations[:4]
    print(variations)
    print(f"Generated {len(search_queries)} queries.")

    print("\nRetrieving & reranking...")
    candidates = {} 
    
    for i, q in enumerate(search_queries):
        chunks = hybrid_retrieve(q, top_k=10, use_reranker=True)
        
        for chunk in chunks:
            node_id = chunk.node.node_id
            
            if node_id not in candidates:
                candidates[node_id] = chunk
            elif chunk.score > candidates[node_id].score:
                candidates[node_id] = chunk

    retrieved_chunks = sorted(candidates.values(), key=lambda x: x.score, reverse=True)[:40]
    print(f"Selected {len(retrieved_chunks)} top chunks.")

    papers = {}
    theory_keywords = ['activation energy', 'phase', 'intrinsic', 'dft', 'conductivity', 'stability']
    theory_chunks = []

    for c in retrieved_chunks:
        meta = c.node.metadata
        idx = meta.get('doc_idx') or meta.get('file_name') or c.node.node_id
        context = meta.get('section_summary') or meta.get('doc_context') or ""
        
        if idx not in papers:
            papers[idx] = {
                'file': meta.get('file_name', 'Unknown'), 
                'context': context, 
                'chunks_text': [],
                'max_score': c.score,
                'num_chunks': 0
            }

        papers[idx]['chunks_text'].append(c.node.text)
        papers[idx]['num_chunks'] += 1
        papers[idx]['max_score'] = max(papers[idx]['max_score'], c.score)
        
        if any(w in c.node.text.lower() for w in theory_keywords):
            theory_chunks.append(c)
            
    relevant_papers = sorted(papers.values(), key=lambda x: x['max_score'], reverse=True)

    print("Extracting physical constraints...")
    
    t_texts = []
    for i, c in enumerate(theory_chunks[:20]):
        text = c.node.text
        has_numbers = bool(re.search(r'\d+\.?\d*\s*(eV|mS\/cm|S\/cm|MPa|°C|K|V)', text))
        
        snippet = f"[Chunk {i}] {text[:800]}"
        if has_numbers:
            t_texts.insert(0, snippet)
        else:
            t_texts.append(snippet)
            
    t_text = "\n".join(t_texts[:15])
    
    constraint_prompt = f"""Analyze physics limits for: "{query}"
    Data: {t_text}
    Provide:
1. INTRINSIC MATERIAL LIMITS (Crystal structure, max theoretical conductivity)
2. INTERFACIAL/PROCESSING LIMITS (Grain boundary, Density, Temp/Pressure)
3. CHEMICAL STABILITY CONSTRAINTS (Voltage window, Decomposition)
4. THERMODYNAMIC IMPOSSIBILITIES (What violates physics?)
5. REALISTIC TARGETS (What is actually achievable?)

Be specific but brief, dont include any preamble."""
    
    constraints = call_llm(constraint_prompt, max_tokens=1100, temperature=0.1)
    print(constraints)
    print("Synthesizing literature review...")
    p_text_list = []
    for i, p in enumerate(relevant_papers[:15]):
        evidence = "\n".join(p['chunks_text'])
        p_text_list.append(f"PAPER {i+1} ({p['file']}): {p['context']}\nDATA: {evidence[:1000]}")
    p_text = "\n\n".join(p_text_list)
        
    analysis_prompt = f"""Brief Systematic Review for: "{query}"
    Constraints: {constraints}
    Data: {p_text}
    Provide brief but detailed/dense and structured report: Materials, Conditions, Mechanisms, Gaps."""
    
    summary = call_llm(analysis_prompt, max_tokens=2000, temperature=0.2)

    state.update({
        'retrieved_chunks': retrieved_chunks, 
        'relevant_papers': relevant_papers, 
        'literature_summary': summary, 
        'physical_constraints': constraints
    })
    state['execution_log'].append(f"Lit Analysis: {len(relevant_papers)} papers analyzed")
    return state


def mechanism_synthesis_agent(state: ResearchState) -> ResearchState:
    print("AGENT 2: MECHANISM SYNTHESIS")
    print("Identifying mechanisms...")
    mech_prompt = f"""Explain MECHANISMS for '{state['query']}'
    Using: {state['literature_summary'][:2000]}
    
    Explain CAUSALITY (Driving Forces, Kinetic Barriers, Stress Coupling)."""
    mech = call_llm(mech_prompt, max_tokens=1500)

    print("Synthesizing design rules...")
    patt_prompt = f"""Synthesize DESIGN RULES from:
    {mech}
    Identify: Structure-Property relations, Trade-offs, Scaling laws."""
    patt = call_llm(patt_prompt, max_tokens=1000)
    
    state.update({'patterns': patt, 'identified_mechanisms': [{'raw_text': mech}]})
    state['execution_log'].append("Mechanisms Identified")
    return state


def hypothesis_generator_agent(state: ResearchState) -> ResearchState:
    print("AGENT 3: HYPOTHESIS GENERATOR")
    
    prompt = f"""You are a tenured professor in Battery Science (Solid-State & Beyond) with expertise in materials, mechanics, and manufacturing.
Reply briefly but in detail in bullet points
RESEARCH QUESTION: "{state['query']}"

CRITICAL - PHYSICAL CONSTRAINTS & CONTEXT:
{state['physical_constraints']}

Previous Critique (if any): {state['critic_feedback']}
LITERATURE CONTEXT:
{state['literature_summary'][:1800]}

KNOWN PATTERNS:
{state['patterns'][:600]}

================================================================================
PRE-CHECK (MANDATORY)
================================================================================

Identify the QUERY TYPE and apply the relevant logic:

**TYPE A: MATERIALS DISCOVERY (e.g., "New electrolyte", "Doping strategy")**
- What is the INTRINSIC LIMIT of the base material? (e.g., theoretical conductivity, voltage window)
- Is the target thermodynamically stable? (Check phase diagrams, decomposition voltages)
- *Constraint:* Do not propose properties exceeding theoretical maxima without a phase change.

**TYPE B: PROCESS/CELL ENGINEERING (e.g., "Stack pressure", "Sintering profile", "Coating")**
- What is the PROCESS-PROPERTY relationship? (e.g., Higher pressure -> lower contact resistance but higher creep)
- What are the mechanical limits? (e.g., Particle fracture strength, separator yield strength)
- *Constraint:* Do not propose processing conditions that destroy the material (e.g., Sintering above melting point).

**TYPE C: MECHANISM/FAILURE ANALYSIS (e.g., "Why does it fail?", "Dendrite growth")**
- What is the DRIVING FORCE? (e.g., Overpotential, Chemical potential gradient)
- What is the KINETIC BARRIER? (e.g., Nucleation energy, Exchange current density)
- *Constraint:* Mechanisms must respect conservation of mass/charge and thermodynamics.

================================================================================
HYPOTHESIS GENERATION RULES (STRICTLY ENFORCED)
================================================================================

❌ FORBIDDEN:
1. Violating thermodynamic laws (e.g., "Stable against Li metal at 5V" without kinetic protection).
2. "Mixing" materials without defining the interface (coating? composite? alloy?).
3. Targets exceeding theoretical limits (>3x) without a clear mechanism (e.g., phase change).
4. Chemically invalid formulas (MUST BE CHARGE NEUTRAL).

✅ ACCEPTABLE:
1. Mechanism-based Interventions (Doping, Coatings, Pressure, Temp).
2. Trade-off optimizations (e.g., "Sacrifice some conductivity for stability").
3. Novel application of known principles (e.g., "Using polymer mechanic theory on ceramics").

================================================================================
REQUIRED HYPOTHESIS STRUCTURE (ADAPTIVE)
================================================================================

For EACH of 5 hypotheses:

**HYPOTHESIS [N]: [Title]**

**TYPE & CONSTRAINT CHECK:**
- Query Type: [Material / Process / Mechanism]
- Key Constraint: [e.g., "Decomposition potential is 2.5V"]
- Feasibility: [Why is this possible? e.g., "Kinetic passivation allows exceeding the thermodynamic limit"]

**THE SPECIFIC PROBLEM:**
[Define the bottleneck clearly]
Example (Material): "Bulk conductivity is high, but grain boundary resistance dominates (90% of total)."
Example (Process): "Cold pressing leaves 15% porosity, limiting active area."

**THEORETICAL BASIS:**
[The "Why" - Thermodynamics, Kinetics, or Mechanics]
Example: "Porosity reduction follows the Heckel equation. Yield strength of chloride is low (200 MPa), allowing densification at RT."

**PROPOSED INTERVENTION:**
[Be SPECIFIC. Recipe / Protocol / Design]
Example: "Step-sintering protocol:
- Heat to 0.8*Tm (fast ramp) to neck particles.
- Hold at 0.6*Tm to densify without grain growth.
- Atmosphere: Ar + S vapor to prevent surface decomposition."

**MECHANISTIC HYPOTHESIS:**
[HOW does the intervention work?]
Example: "Two-step sintering decouples densification from grain growth (Ostwald ripening). 
Predicted result: 98% density with grain size < 2um."

**QUANTITATIVE PREDICTIONS:**
[Specific metrics to measure success]
- Primary Outcome: [e.g., Density > 98%, Conductivity > 3 mS/cm]
- Secondary Signature: [e.g., "Narrow grain size distribution"]

**FALSIFICATION CRITERIA:**
[What result proves you wrong?]
Example: "If density > 98% but conductivity decreases, then impurities from sintering (not porosity) are the bottleneck."

**EXPERIMENTAL APPROACH:**
[Brief Plan: Synthesis -> Assembly -> Characterization]

**NOVELTY & IMPACT:**
[Why is this new/important?]
    """
    print("Generating hypotheses...")
    hypotheses = call_llm(prompt, max_tokens=3000, temperature=0.4)
    print(hypotheses)
    state.update({'proposed_hypotheses': [{'raw_text': hypotheses}]})
    state['execution_log'].append("Hypotheses Generated")
    return state


def materials_project_verifier_agent(state: ResearchState) -> ResearchState:
    print("AGENT 3.5: MATERIALS PROJECT VERIFIER")
    
    hypotheses = state['proposed_hypotheses'][0]['raw_text']

    print("Scanning hypotheses for chemical formulas...")

    extraction_prompt = f"""Extract ALL specific chemical formulas mentioned in these hypotheses.
    Hypotheses:
    {hypotheses[:2500]}
    
    Return ONLY a JSON list of strings. Example: ["Na3PS4", "LiCoO2", "ZrO2"]
    If no specific materials are mentioned, return []
    """
    
    raw = call_llm(extraction_prompt, max_tokens=150, temperature=0.0)
    
    formulas = []
    try:
        clean_json = raw.strip().replace("```json", "").replace("```", "")
        formulas = json.loads(clean_json)
    except:
        print("JSON parse failed, falling back to regex")
        formulas = re.findall(r'\b[A-Z][a-z]?\d*(?:[A-Z][a-z]?\d*)*\b', hypotheses)
        formulas = [f for f in formulas if any(c.isdigit() for c in f) and len(f) > 2]

    if not formulas:
        print("No specific materials found to verify.")
        state['mp_summary_text'] = "Verification: Not required (No formulas found)."
        return state

    print(f"Verifying {len(formulas)} formulas: {formulas}")
    
    results_text = []
    unique_formulas = sorted(list(set(formulas)))[:3]
    
    for formula in unique_formulas:
        try:
            print(f"  Checking {formula}...")
            data = search_materials_from_nl(f"formula {formula}")
            
            if data:
                summary = summarize_material_dict(data[0])
                results_text.append(f"--- {formula} ---\n{summary}")
            else:
                results_text.append(f"--- {formula} ---\nNot found in Materials Project database.")
                
        except Exception as e:
            print(f"  Error checking {formula}: {e}")
            continue

    final_summary = "\n\n".join(results_text) if results_text else "Verification: Material data not found."
    print("Verification complete.")
    print(final_summary)
    
    state['mp_summary_text'] = final_summary
    state['execution_log'].append(f"MP Verifier: Checked {len(unique_formulas)} formulas")
    
    return state

def critic_agent(state: ResearchState) -> ResearchState:
    print("AGENT 4: CRITIC")
    
    print("Evaluating hypotheses...")
    prompt = f"""ACT AS: Reviewer for Nature Energy.
    
    MP Data (Stability Check): {state['mp_summary_text']}
    Lit Context: {state['literature_summary'][:1500]}

    Evaluate all hypotheses independently, there should be 5.
    For EACH hypotheses: {state['proposed_hypotheses'][0]['raw_text']}
    
    For each, Evaluate Rigor, Mechanism, Specificity, Novelty. Provide potential improvements and anything glaring that needs to be accounted for, and how it can be changed to account for it. Be detailed but brief.
    Provide score for each(Example: "Hypothesis 1 Score: X/10"), Do NOT score above 5 if the glaring omission is too serious and renders the hypothesis effectively useless
    REQUIRED: At the end after all critiques, print 'OVERALL SCORE: [X.X/10]'.
    """
    critique = call_llm(prompt, max_tokens=2000, temperature=0.1)
    print(critique)
    match = re.search(r'OVERALL SCORE:\s*(\d+\.?\d*)', critique)
    score = float(match.group(1)) if match else 5.0
    
    print(f"Critique Complete. Score: {score}/10")
    
    needs_revision = score < 7.0 and state['iteration'] < state['max_iterations']
    if needs_revision:
        print("Revision Requested.")
    else:
        print("Hypotheses Approved.")
        
    state.update({'critic_score': score, 'critic_feedback': critique, 'needs_revision': needs_revision})
    state['execution_log'].append(f"Critic Score: {score}")
    return state


def experiment_planner_agent(state: ResearchState) -> ResearchState:
    print("AGENT 5: EXPERIMENT PLANNER")
    
    print("Drafting experimental protocols...")
    plans = call_llm(f"Create Lab SOPs for:\n{state['proposed_hypotheses'][0]['raw_text']}", max_tokens=2000)
    
    print("Generating recommendations...")
    rec = call_llm(f"Based on plans: {plans}...\nRecommend Top 3 Experiments & Order briefly but in detail", max_tokens=1500)
    
    state.update({'recommended_next_steps': rec, 'experimental_designs': [{'raw_text': plans}]})
    state['execution_log'].append("Plans Created")
    return state


def create_workflow():
    wf = StateGraph(ResearchState)

    wf.add_node("literature_analysis", literature_analysis_agent)
    wf.add_node("mechanism_synthesis", mechanism_synthesis_agent)
    wf.add_node("hypothesis_generator", hypothesis_generator_agent)
    wf.add_node("mp_verifier", materials_project_verifier_agent)
    wf.add_node("critic", critic_agent)
    wf.add_node("planner", experiment_planner_agent)

    wf.set_entry_point("literature_analysis")
    wf.add_edge("literature_analysis", "mechanism_synthesis")
    wf.add_edge("mechanism_synthesis", "hypothesis_generator")
    wf.add_edge("hypothesis_generator", "mp_verifier")
    wf.add_edge("mp_verifier", "critic")

    def router(state):
        if state['needs_revision']:
            print(f"\nLoop Back: Iteration {state['iteration'] + 1}")
            state['iteration'] += 1
            return "hypothesis_generator"
        return "planner"
    
    wf.add_conditional_edges("critic", router, {
        "hypothesis_generator": "hypothesis_generator",
        "planner": "planner"
    })
    
    wf.add_edge("planner", END)
    return wf.compile()

def run_research_pipeline(query: str, max_iterations: int = 2):
    print(f"STARTING RESEARCH: {query}")
    
    initial_state = {
        'query': query,
        'research_goal': 'generate_hypotheses',
        'iteration': 1,
        'max_iterations': max_iterations,
        'execution_log': [],
        'retrieved_chunks': [], 'relevant_papers': [], 'literature_summary': '',
        'mp_summary_text': '', 'identified_mechanisms': [], 'patterns': '',
        'proposed_hypotheses': [], 'critic_score': 0.0, 'critic_feedback': '',
        'needs_revision': False, 'experimental_designs': [], 'recommended_next_steps': ''
    }
    
    app = create_workflow()
    return app.invoke(initial_state, {"recursion_limit": 50})

def display_results(state: ResearchState):
    print("\n\n")
    print("FINAL RESEARCH OUTPUT")

    print("\nLITERATURE FINDINGS")
    print(f"Analyzed {len(state['relevant_papers'])} papers.")
    print(f"Constraints Identified: {len(state['physical_constraints']) > 10}")
    
    print("\nHYPOTHESES (Approved)")
    if state['proposed_hypotheses']:
        print(state['proposed_hypotheses'][0]['raw_text'])
        
    print("\nEXPERIMENTAL PLAN")
    print(state['recommended_next_steps'])

if __name__ == "__main__":
    # Test Query
    q = "For a high-voltage oxide cathode (e.g., NMC or Li-rich layered oxide) paired with a sulfide solid electrolyte, propose hypotheses on how coating chemistry (e.g., LiNbO₃ vs Li₃PO₄ vs Li₂ZrO₃) influences interfacial decomposition and impedance growth at 4.3–4.5 V. Design a comparative experimental plan including coating synthesis, cell assembly, cycling protocol, and post-mortem analysis to differentiate which coating is most effective and why"
    #q = "How can I achieve >10mS/cm for solid state sodium ion electrolytes with only ball milling and cold pressing at room temperature? Focus on halides"
    final_state = run_research_pipeline(q, max_iterations=2)
    display_results(final_state)