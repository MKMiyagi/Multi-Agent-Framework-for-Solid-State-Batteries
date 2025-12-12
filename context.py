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

print("Testing HF connections...\n")

print("1. Testing LLM (Qwen 2.5 72B)...")
try:
    completion = llm_client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": "Say hello"}],
        max_tokens=50,
        temperature=0.0
    )
    print(f"LLM works: {completion.choices[0].message.content}\n")
except Exception as e:
    print(f"LLM failed: {e}\n")
    exit(1)

print("2. Testing embeddings (Qwen 3 8B)...")
try:
    test_embed = embed_client.feature_extraction("test", model=EMBED_MODEL)
    if isinstance(test_embed, list) and len(test_embed) > 0 and isinstance(test_embed[0], list):
        test_embed = test_embed[0]
    if hasattr(test_embed, 'tolist'):
        test_embed = test_embed.tolist()
    print(f"Embeddings work: {len(test_embed)} dimensions\n")
except Exception as e:
    print(f"Embeddings failed: {e}\n")
    exit(1)

print("Config:")
print(f"  LLM: {LLM_MODEL}")
print(f"  Embeddings: {EMBED_MODEL}")
print(f"  Embedding dimensions: {len(test_embed)}")

def get_document_context(content: str, filename: str) -> str:
    MAX_CHARS = 100000
    
    if len(content) > MAX_CHARS:
        print(f"Document too long ({len(content):,} chars), using smart truncation...")
        first_part_len = int(MAX_CHARS * 0.8)
        last_part_len = int(MAX_CHARS * 0.2)
        
        truncated_content = (
            content[:first_part_len] + 
            "\n\n[... middle section truncated ...]\n\n" + 
            content[-last_part_len:]
        )
        content = truncated_content
        print(f"   → Truncated to {len(content):,} chars")
    
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
                temperature=0.0
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            error_msg = str(e)
            
            if "length" in error_msg.lower() or "too long" in error_msg.lower():
                if attempt == 0:
                    print(f" Still too long, using abstract + conclusion only...")
                    content_lower = content.lower()
                    
                    abstract_start = max(
                        content_lower.find("abstract"),
                        content_lower.find("summary"),
                        0
                    )
                    abstract_end = abstract_start + 5000
                    
                    conclusion_start = max(
                        content_lower.rfind("conclusion"),
                        content_lower.rfind("summary"),
                        len(content) - 5000
                    )
                    
                    content = content[abstract_start:abstract_end] + "\n\n" + content[conclusion_start:]
                    print(f"   → Reduced to {len(content):,} chars")
                    
                    prompt = f"""Analyze this solid-state battery research paper and provide a concise summary (3-4 sentences):
1. Main research question or objective
2. Key materials/chemistries studied (catholytes, cathodes, electrolytes, specific compounds)
3. Critical experimental conditions (temperature, pressure, particle size, cycling rates)
4. Main findings or conclusions

Paper:
{content}

Respond with ONLY the summary, no preamble:"""
                    continue
                    
            if attempt < 2:
                print(f"Context generation attempt {attempt+1} failed, retrying in 5s...")
                time.sleep(5)
            else:
                print(f"Context generation failed after 3 attempts: {error_msg[:100]}")
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
            error_str = str(e)
            if any(code in error_str for code in ['502', '503', 'Bad Gateway', 'Connection']):
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 2  # 2s, 4s, 6s
                    print(f"      Retry {attempt+1}/{max_retries} in {wait_time}s...", flush=True)
                    time.sleep(wait_time)
                else:
                    raise 
            else:
                raise 


print("Loading documents...\n")
reader = SimpleDirectoryReader(input_dir="./processed_text_only", recursive=True)
documents = reader.load_data()

print(f"Loaded {len(documents)} documents")
splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=50)

all_nodes = []

for doc_idx, doc in enumerate(documents):
    filename = doc.metadata.get('file_name', 'unknown')
    
    print(f"Processing [{doc_idx + 1}/{len(documents)}]: {filename}")
    
    content = doc.get_content()
    print(f"  Document length: {len(content):,} characters")
 
    print(f"  Step 1: Generating document context...", flush=True)
    doc_context = get_document_context(content, filename)
    print(f"Context: {doc_context[:150]}...\n")
 
    print(f"  Step 2: Chunking document...", flush=True)
    temp_doc = Document(text=content, metadata=doc.metadata)
    nodes = splitter.get_nodes_from_documents([temp_doc])
    print(f"Created {len(nodes)} chunks\n")

    print(f"  Step 3: Adding embeddings and context...", flush=True)
    for node_idx, node in enumerate(nodes):
        if node_idx % 10 == 0:
            print(f"Processing chunk {node_idx}/{len(nodes)}", flush=True)
        
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
            all_nodes.append(node)
            
        except Exception as e:
            print(f"    ⚠ Failed to process chunk {node_idx} after retries: {e}")
            continue
    
    chunk_count = len([n for n in all_nodes if n.metadata.get('doc_idx') == doc_idx])
    print(f"Completed: {chunk_count} nodes added\n")


    if len(all_nodes) > 0:
        print("Checking node structure")

        sample_node = all_nodes[0]
        
        print(f"\n1. Node Type: {type(sample_node)}")
        print(f"2. Text preview: {sample_node.get_content()[:150]}...")
        
        print(f"\n3. Metadata:")
        print(f"   - file_name: {sample_node.metadata.get('file_name')}")
        print(f"   - doc_context: {sample_node.metadata.get('doc_context', '')[:100]}...")
        print(f"   - chunk_idx: {sample_node.metadata.get('chunk_idx')}")
        
        print(f"\n4. Embedding:")
        if sample_node.embedding:
            print(f"Embedding dimensions: {len(sample_node.embedding)}")
            print(f"First 5 values: {sample_node.embedding[:5]}")
        else:
            print(f"No embedding found!")
        
        print(f"\n5. Statistics:")
        print(f"   - Total nodes: {len(all_nodes)}")
        print(f"   - Nodes with embeddings: {sum(1 for n in all_nodes if hasattr(n, 'embedding') and n.embedding)}")
        print(f"   - Unique documents: {len(set(n.metadata.get('doc_idx') for n in all_nodes))}")
        
print(f"  Total documents: {len(documents)}")
print(f"  Total nodes: {len(all_nodes)}")
print(f"  Average chunks/doc: {len(all_nodes)/len(documents):.1f}")
print(f"  LLM model: {LLM_MODEL}")
print(f"  Embedding model: {EMBED_MODEL}")
print(f"  Embedding dimensions: {len(all_nodes[0].embedding) if all_nodes else 'N/A'}")

print("Saving to contextual_nodes.pkl...")
with open("contextual_nodes.pkl", "wb") as f:
    pickle.dump(all_nodes, f)

print("Saved successfully")