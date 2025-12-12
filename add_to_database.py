import os
import pickle
import time
from llama_index.core import SimpleDirectoryReader, Document
from llama_index.core.node_parser import SentenceSplitter
from huggingface_hub import InferenceClient

HF_API_KEY = os.getenv("HF_API_KEY")
if not HF_API_KEY:
    raise ValueError("HF_API_KEY environment variable not set. Please export HF_API_KEY='your_key_here'")

LLM_MODEL = "Qwen/Qwen2.5-72B-Instruct"
EMBED_MODEL = "Qwen/Qwen3-Embedding-8B"

llm_client = InferenceClient(api_key=HF_API_KEY)
embed_client = InferenceClient(provider="nebius", api_key=HF_API_KEY)

def get_document_context(content: str, filename: str) -> str:
    prompt = f"""Analyze this solid-state battery research paper and provide a concise summary (3-4 sentences):
1. Main research question or objective
2. Key materials/chemistries studied (catholytes, cathodes, electrolytes, specific compounds)
3. Critical experimental conditions (temperature, pressure, particle size, cycling rates)
4. Main findings or conclusions

Paper:
{content}

Respond with ONLY the summary, no preamble:"""
    
    for attempt in range(3):
        try:
            completion = llm_client.chat.completions.create(
                model=LLM_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300,
                temperature=0.1
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            if attempt < 2:
                print(f"Retry {attempt+1}...")
                time.sleep(5)
            else:
                return f"Research paper: {filename}"

def get_embedding(text: str, max_retries=3):
    for attempt in range(max_retries):
        try:
            embedding = embed_client.feature_extraction(text, model=EMBED_MODEL)
            if hasattr(embedding, 'tolist'):
                embedding = embedding.tolist()
            if isinstance(embedding, list) and len(embedding) > 0 and isinstance(embedding[0], list):
                embedding = embedding[0]
            return embedding
        except Exception as e:
            if any(code in str(e) for code in ['502', '503', 'Bad Gateway']):
                if attempt < max_retries - 1:
                    time.sleep((attempt + 1) * 2)
                else:
                    raise
            else:
                raise

print("Loading existing nodes...")
try:
    with open("contextual_nodes.pkl", "rb") as f:
        existing_nodes = pickle.load(f)
    print(f"Loaded {len(existing_nodes)} existing nodes\n")
    
    processed_files = set(node.metadata.get('file_name') for node in existing_nodes)
    print(f"Already processed files: {len(processed_files)}")
    
    max_doc_idx = max((node.metadata.get('doc_idx', -1) for node in existing_nodes), default=-1)
    
except FileNotFoundError:
    print("No existing nodes found, starting fresh\n")
    existing_nodes = []
    processed_files = set()
    max_doc_idx = -1

print("\nScanning for new documents...")
reader = SimpleDirectoryReader(input_dir="./processed_text_only", recursive=True)
all_documents = reader.load_data()

new_documents = [doc for doc in all_documents 
                 if doc.metadata.get('file_name') not in processed_files]

if len(new_documents) == 0:
    print("No new documents to process")
    exit(0)

print(f"Found {len(new_documents)} new documents to process")
print("="*80 + "\n")

splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=50)
new_nodes = []

for idx, doc in enumerate(new_documents):
    doc_idx = max_doc_idx + 1 + idx
    filename = doc.metadata.get('file_name', 'unknown')
    
    print(f"Processing [{idx + 1}/{len(new_documents)}]: {filename}")
    
    content = doc.get_content()
    print(f"  Document length: {len(content):,} characters")
    
    print(f"  Step 1: Generating document context...", flush=True)
    doc_context = get_document_context(content, filename)
    print(f"  Context: {doc_context[:150]}...\n")
    
    print(f"  Step 2: Chunking document...", flush=True)
    temp_doc = Document(text=content, metadata=doc.metadata)
    nodes = splitter.get_nodes_from_documents([temp_doc])
    print(f"  Created {len(nodes)} chunks\n")
    
    print(f"  Step 3: Adding embeddings...", flush=True)
    for node_idx, node in enumerate(nodes):
        if node_idx % 10 == 0:
            print(f"    Chunk {node_idx}/{len(nodes)}", flush=True)
        
        try:
            node_text = node.get_content()
            embedding = get_embedding(node_text)
            
            node.metadata.update({
                'file_name': filename,
                'doc_context': doc_context,
                'chunk_idx': node_idx,
                'doc_idx': doc_idx,
                'total_chunks': len(nodes),
                'embed_model': EMBED_MODEL
            })
            
            node.embedding = embedding
            new_nodes.append(node)
            
        except Exception as e:
            print(f"Failed chunk {node_idx}: {e}")
            continue
    
    print(f"Added {len([n for n in new_nodes if n.metadata.get('doc_idx') == doc_idx])} nodes\n")

print(f"Merging Nodes")
print(f"  Existing nodes: {len(existing_nodes)}")
print(f"  New nodes: {len(new_nodes)}")
print(f"  Total: {len(existing_nodes) + len(new_nodes)}")
print(f"{'='*80}\n")

all_nodes = existing_nodes + new_nodes

print("Saving updated nodes to contextual_nodes.pkl...")
with open("contextual_nodes.pkl", "wb") as f:
    pickle.dump(all_nodes, f)

print("Successfully added new documents")
print(f"   Total documents: {len(set(n.metadata.get('doc_idx') for n in all_nodes))}")
print(f"   Total nodes: {len(all_nodes)}\n")