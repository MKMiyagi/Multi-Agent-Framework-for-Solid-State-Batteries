import pickle
import json
import re
import torch
import operator
import os
from typing import TypedDict, List, Dict, Annotated, Literal, Any, Optional
from langgraph.graph import StateGraph, END
from huggingface_hub import InferenceClient
from llama_index.core import Settings
from llama_index.core.schema import NodeWithScore
from llama_index.embeddings.huggingface_api import HuggingFaceInferenceAPIEmbedding
from llama_index.postprocessor.flag_embedding_reranker import FlagEmbeddingReranker

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



def hypothesis_generator_agent(state: ResearchState) -> ResearchState:
    print("AGENT 3: HYPOTHESIS GENERATOR")
    
    prompt = f"""You are a tenured professor in Battery Science (Solid-State & Beyond) with expertise in materials, mechanics, and manufacturing.
Reply BRIEFLY but in detail in bullet points
RESEARCH QUESTION: "{state['query']}"

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
    hypotheses = call_llm(prompt, max_tokens=3200, temperature=0.4)
    print(hypotheses)
    state.update({'proposed_hypotheses': [{'raw_text': hypotheses}]})
    state['execution_log'].append("Hypotheses Generated")
    return state



def critic_agent(state: ResearchState) -> ResearchState:
    print("AGENT 4: CRITIC")
    
    print("Evaluating hypotheses...")
    prompt = f"""ACT AS: Reviewer for Nature Energy.
    Evaluate each hypothesis independently.
    For EACH hypotheses: {state['proposed_hypotheses'][0]['raw_text']}
    
    For each, Evaluate Rigor, Mechanism, Specificity, Novelty. Provide potential improvements and anything glaring that needs to be accounted for, and how it can be changed to account for it. Be detailed but brief.
    Provide score for each(Example: "Hypothesis 1 Score: X/10"). Do NOT score above 5 if the glaring omission is too serious and renders the hypothesis effectively useless
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


def create_workflow():
    wf = StateGraph(ResearchState)

    wf.add_node("hypothesis_generator", hypothesis_generator_agent)
    wf.add_node("critic", critic_agent)

    wf.set_entry_point("hypothesis_generator")
    wf.add_edge("hypothesis_generator", "critic")

    def router(state):
        if state['needs_revision']:
            print(f"\n Loop Back: Iteration {state['iteration'] + 1}")
            state['iteration'] += 1
            return "hypothesis_generator"
        return "critic"
    
    wf.add_conditional_edges("critic", router, {
        "hypothesis_generator": "hypothesis_generator",
        "critic": "critic"
    })
    
    wf.add_edge("critic", END)
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
    final_state = run_research_pipeline(q, max_iterations=3)
    display_results(final_state)