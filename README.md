# A Mutli-Agent Framework for Hypothesis Generation & Experimental Design in Solid-State Battery Research

This repository contains the final project for CMSC 35370: AI Agents for Science taught at the Univeristy of Chicago.

## Features

- **Literature Analysis Agent**: RAG Agent that has 100 hand-selected papers on solid-state battery research that finds relevent information chunks
- **Mechanical Synthesis Agent**: Finds patterns and combinations from the chunks the Literature Analysis Agent sources
- **Hypothesis Generation Agent**: Generates 5 hypotheses that are based on the prompt from the user and the information from the Literature Analysis and Mechanical Synthesis Agents
- **Materials Project Agent**: Searches for the materials properties of the chemicals mentioned in the hypotheses to pass to the critic agent
- **Critic Agent**: Evalulates the Hypotheses on a scale from 1/10 based on the novelty, scientific depth, and feasibility of the hypotheses based on the materials properties and its own reasoning
- **Experimetal Design Agent**: Produces an experimental plan for the best hypothesis determined by the critic

## Prerequisites
- Python Virtual Environment 3.12.3
- API Keys for:
  - Hugging Face (HF_API_KEY)
  - Materials Project (MP_API_KEY)

## Installation
1. Clone the repo
2. Install dependencies
```bash
pip install -r requirements.txt
```

## Setup API Keys

Before running the system, ou must set up your API keys as environment variables within the terminal

**For macOS/Linux/WSL**
```bash
export HF_API_KEY="your API key"
export MP_API_KEY="your API key"
```

## Example Prompt
```
For a high-voltage oxide cathode (e.g. NMC or Li-rich oxide) paired with a sulfide 
solid-electrolyte, propose hypotheses on how coating chemistry (e.g. LiNbO3 vs Li3PO4 
vs Li2ZrO2) influences interfacial decomposition and impedance growth at 4.3-4.5 V. 
Design a comparative experimental plan including coating synthesis, cell assembly, 
cycling protocol, and post-mortem analysis to differentiate which coating is most 
effective and why.
```

## Project Structure
```
├── research_framework.py
├── example outputs/
│   ├── system_output.txt
│   ├── hypothesis_critic_loop.txt
│   └── hypothesis_only.txt
├── requirements.txt
└── README.md
```
