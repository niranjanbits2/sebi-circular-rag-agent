"""
SEBI RAG Step 3 — Terminal Chatbot (Fixed for LangChain 0.2+)
LangChain + FAISS + Amazon Bedrock Nova Lite
"""
import os, json, time, boto3
from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings

REGION="us-east-1"; EMBED_MODEL="amazon.titan-embed-text-v1"
LLM_MODEL="amazon.nova-lite-v1:0"; INDEX_PATH="sebi_faiss_index"
G="\033[92m";Y="\033[93m";R="\033[91m";B="\033[94m";W="\033[0m"
BOLD="\033[1m";CYAN="\033[96m";PURP="\033[95m"

SYSTEM_PROMPT="""You are SEBI Circular Intelligence Assistant — expert on SEBI regulations.
Answer questions based ONLY on the provided SEBI circular excerpts.
Be precise, cite specific circular numbers, and give practical compliance guidance.
Format: Direct answer → Specific rule/number → Source circular → Practical implication.
If not in context say: This is not covered in the loaded circulars. Refer to sebi.gov.in"""

def load_pipeline():
    bedrock=boto3.client("bedrock-runtime",region_name=REGION)
    embeddings=BedrockEmbeddings(client=bedrock,model_id=EMBED_MODEL,region_name=REGION)
    vs=FAISS.load_local(INDEX_PATH,embeddings,allow_dangerous_deserialization=True)
    return vs, bedrock

def retrieve(vs, question, k=4):
    docs=vs.similarity_search(question,k=k)
    parts=[]; sources=set()
    for doc in docs:
        parts.append(doc.page_content)
        circ=doc.metadata.get("circular_no","")
        date=doc.metadata.get("date","")
        subj=doc.metadata.get("subject","")
        if circ: sources.add(f"{circ} ({date}) — {subj[:55]}")
    return "\n\n---\n\n".join(parts), list(sources)

def ask_nova(bedrock, question, context):
    prompt=f"""Based on the SEBI circular excerpts below, answer the question precisely.

SEBI CIRCULAR EXCERPTS:
{context}

QUESTION: {question}

Answer:"""
    body=json.dumps({
        "system":[{"text":SYSTEM_PROMPT}],
        "messages":[{"role":"user","content":[{"text":prompt}]}],
        "inferenceConfig":{"maxTokens":800,"temperature":0.1}
    })
    resp=bedrock.invoke_model(modelId=LLM_MODEL,body=body,
        contentType="application/json",accept="application/json")
    result=json.loads(resp["body"].read())
    return result["output"]["message"]["content"][0]["text"].strip()

def banner():
    print(f"\n{BOLD}{'='*60}{W}")
    print(f"{BOLD}  SEBI Circular Intelligence Assistant{W}")
    print(f"{BOLD}  TechM Agentic AI — LangChain + FAISS + Bedrock{W}")
    print(f"{BOLD}{'='*60}{W}")
    print(f"\n  {G}✓{W} 10 SEBI circulars indexed")
    print(f"  {G}✓{W} Embeddings: Amazon Titan | Vector DB: FAISS")
    print(f"  {G}✓{W} LLM: Nova Lite (us-east-1)")
    print(f"\n  {Y}Try asking:{W}")
    print(f"  • What are SEBI rules on insider trading?")
    print(f"  • What is the F&O margin requirement?")
    print(f"  • How should listed companies disclose material events?")
    print(f"  • What are SEBI cybersecurity requirements?")
    print(f"  • What is BRSR and who must file it?")
    print(f"  • What are IPO lock-in rules?")
    print(f"  • How does SCORES 2.0 work?")
    print(f"  • What are PMS minimum investment rules?")
    print(f"\n  Type {R}exit{W} to quit\n")
    print(f"{'─'*60}")

def main():
    print(f"\n  Loading RAG pipeline...",end="",flush=True)
    try:
        vs, bedrock = load_pipeline()
        print(f" {G}✓ Ready!{W}")
    except Exception as e:
        print(f"\n  {R}Error: {e}{W}")
        print(f"  Run sebi_step2_build_rag.py first!\n")
        return

    banner()

    while True:
        try:
            q=input(f"\n  {BOLD}You:{W} ").strip()
        except (KeyboardInterrupt,EOFError):
            print(f"\n\n  {G}Goodbye! 👋{W}\n"); break

        if not q: continue
        if q.lower() in ["exit","quit","bye","q"]:
            print(f"\n  {G}Goodbye! 👋{W}\n"); break

        print(f"\n  {CYAN}Searching circulars...{W}",end="",flush=True)
        start=time.time()
        context,sources=retrieve(vs,q)

        print(f"\r  {CYAN}Generating answer...   {W}",end="",flush=True)
        try:
            answer=ask_nova(bedrock,q,context)
            elapsed=round(time.time()-start,1)
            print(f"\r  {G}✓ ({elapsed}s)            {W}\n")
            print(f"  {PURP}{BOLD}SEBI Assistant:{W}")
            for line in answer.split("\n"):
                print(f"  {line}")
            if sources:
                print(f"\n  {Y}📋 Sources:{W}")
                for src in sources[:3]:
                    print(f"     {src[:85]}")
        except Exception as e:
            print(f"\r  {R}Error: {str(e)[:80]}{W}")

        print(f"\n{'─'*60}")

if __name__=="__main__": main()
