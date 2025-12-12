import torch
import operator
import os
from typing import TypedDict, List, Dict, Annotated, Literal, Any, Optional
from huggingface_hub import InferenceClient

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Acceleration Device: {DEVICE.upper()}")

HF_API_KEY = os.getenv("HF_API_KEY")
if not HF_API_KEY:
    raise ValueError("HF_API_KEY environment variable not set. Please export HF_API_KEY='your_key_here'")

LLM_MODEL = "deepseek-ai/DeepSeek-V3.2-Exp"

hf_client = InferenceClient(api_key=HF_API_KEY)


def call_llm(prompt: str, max_tokens: int = 3000, temperature: float = 0.3) -> str:
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


if __name__ == "__main__":
    q = "For a high-voltage oxide cathode (e.g., NMC or Li-rich layered oxide) paired with a sulfide solid electrolyte, propose hypotheses on how coating chemistry (e.g., LiNbO₃ vs Li₃PO₄ vs Li₂ZrO₃) influences interfacial decomposition and impedance growth at 4.3–4.5 V. Design a comparative experimental plan including coating synthesis, cell assembly, cycling protocol, and post-mortem analysis to differentiate which coating is most effective and why"
    prompt = f"""You are a tenured professor in Battery Science (Solid-State & Beyond) with expertise in materials, mechanics, and manufacturing.
Reply briefly but in detail in bullet points using known knowledge and research papers, backup with evidence.
RESEARCH QUESTION: {q}

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
    response = call_llm(prompt, max_tokens=3000, temperature=0.4)
    print(response)