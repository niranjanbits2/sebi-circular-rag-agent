"""
SEBI RAG Step 2 — Build RAG Pipeline (Fixed for LangChain 0.2+)
LangChain + FAISS + Amazon Bedrock Titan Embeddings
"""
import os, json, time, boto3
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings

REGION="us-east-1"; EMBED_MODEL="amazon.titan-embed-text-v1"
INDEX_PATH="sebi_faiss_index"; CIRCULARS_PATH="sebi_circulars"
G="\033[92m";Y="\033[93m";R="\033[91m";B="\033[94m";W="\033[0m";BOLD="\033[1m"

def main():
    print(f"\n{BOLD}{'='*55}{W}")
    print(f"{BOLD}  SEBI RAG Step 2 — Build Vector Index{W}")
    print(f"{BOLD}{'='*55}{W}")
    print(f"  Framework  : LangChain")
    print(f"  Embeddings : Amazon Titan Text v1")
    print(f"  Vector DB  : FAISS (local)")
    print(f"  LLM        : AWS Bedrock Nova Lite")

    print(f"\n{B}[1/4] Loading SEBI circulars...{W}")
    loader = DirectoryLoader(CIRCULARS_PATH, glob="*.txt",
        loader_cls=TextLoader, loader_kwargs={"encoding":"utf-8"})
    docs = loader.load()
    print(f"  {G}✓ Loaded {len(docs)} documents{W}")

    with open(os.path.join(CIRCULARS_PATH,"index.json")) as f:
        index = json.load(f)
    index_map = {item["filename"]:item for item in index}
    for doc in docs:
        fname = os.path.basename(doc.metadata.get("source",""))
        if fname in index_map: doc.metadata.update(index_map[fname])

    print(f"\n{B}[2/4] Splitting into chunks...{W}")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800, chunk_overlap=100,
        separators=["\n\n","\n",". "," ",""])
    chunks = splitter.split_documents(docs)
    avg = sum(len(c.page_content) for c in chunks)//len(chunks)
    print(f"  {G}✓ {len(chunks)} chunks | avg {avg} chars{W}")

    print(f"\n{B}[3/4] Initialising Amazon Titan embeddings...{W}")
    bedrock    = boto3.client("bedrock-runtime", region_name=REGION)
    embeddings = BedrockEmbeddings(client=bedrock, model_id=EMBED_MODEL, region_name=REGION)
    print(f"  Testing...", end="", flush=True)
    test = embeddings.embed_query("SEBI insider trading")
    print(f" {G}✓ {len(test)} dimensions{W}")

    print(f"\n{B}[4/4] Building FAISS index...{W}")
    print(f"  Embedding {len(chunks)} chunks — please wait...")
    start=time.time(); all_texts=[c.page_content for c in chunks]; all_metas=[c.metadata for c in chunks]
    vectorstore=None
    for i in range(0,len(chunks),10):
        bt=all_texts[i:i+10]; bm=all_metas[i:i+10]
        if vectorstore is None:
            vectorstore=FAISS.from_texts(texts=bt,embedding=embeddings,metadatas=bm)
        else:
            vectorstore.add_texts(texts=bt,metadatas=bm)
        print(f"  {min(i+10,len(chunks))}/{len(chunks)} chunks",end="\r",flush=True)
        time.sleep(0.2)
    elapsed=round(time.time()-start,1)
    print(f"\n  {G}✓ Built in {elapsed}s{W}")
    vectorstore.save_local(INDEX_PATH)
    print(f"  {G}✓ Saved → {INDEX_PATH}/{W}")

    print(f"\n  Quick test...")
    results=vectorstore.similarity_search("insider trading UPSI",k=2)
    for r in results: print(f"  {G}✓{W}  {r.metadata.get('subject','')[:65]}")

    print(f"\n{BOLD}{'='*55}{W}")
    print(f"{BOLD}{G}  Step 2 COMPLETE!{W}")
    print(f"{BOLD}{'='*55}{W}")
    print(f"\n  {G}✓{W}  {len(chunks)} chunks embedded")
    print(f"  {G}✓{W}  FAISS index → {INDEX_PATH}/")
    print(f"  {G}✓{W}  Time: {elapsed}s")
    print(f"\n  Next: python sebi_step3_chatbot.py")
    print(f"{'='*55}\n")

if __name__=="__main__": main()
