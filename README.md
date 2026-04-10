# SEBI Circular Intelligence Agent 🏦

> **LangChain + FAISS + Amazon Bedrock Nova Lite**  
> RAG pipeline for SEBI regulatory circular Q&A — TechM Agentic AI Practice

---

## What It Does

Answers natural language questions about SEBI (Securities and Exchange Board of India) regulations by searching 10 indexed circulars and generating grounded, cited answers.

```
You:  What are SEBI rules on insider trading?

SEBI Assistant:
  Direct answer → SEBI PIT Regulations 2015 prohibit trading while in 
  possession of UPSI (Unpublished Price Sensitive Information).
  
  Specific rule → Pre-clearance required for trades above INR 10 lakh.
  Trading window closes 48 hours after quarterly results declaration.
  
  Penalty → Up to INR 25 crore or 3x profits, whichever is higher.
  
  📋 Source: SEBI/HO/ISD/ISD-I/P/CIR/2024/001 (January 15, 2024)
```

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                   RAG Pipeline                       │
│                                                     │
│  SEBI Circulars (txt)                               │
│       ↓                                             │
│  LangChain DirectoryLoader                          │
│       ↓                                             │
│  RecursiveCharacterTextSplitter (800 chars)         │
│       ↓                                             │
│  Amazon Bedrock Titan Embeddings (1536 dims)        │
│       ↓                                             │
│  FAISS Vector Index (local)                         │
│       ↓                                             │
│  Similarity Search (top 4 chunks)                   │
│       ↓                                             │
│  Amazon Bedrock Nova Lite → Answer + Citations      │
└─────────────────────────────────────────────────────┘
```

---

## Circulars Indexed

| # | Topic |
|---|-------|
| 1 | Insider Trading — PIT Regulations |
| 2 | F&O Margin Requirements |
| 3 | Algorithmic Trading Framework |
| 4 | Mutual Fund Disclosure Norms |
| 5 | Listed Company Disclosures (LODR) |
| 6 | Cybersecurity Framework (CSCRF) |
| 7 | ESG / BRSR Reporting |
| 8 | IPO Due Diligence Guidelines |
| 9 | Portfolio Management Services |
| 10 | Investor Grievance — SCORES 2.0 |

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| RAG Framework | LangChain 0.2+ |
| Vector Store | FAISS (local, CPU) |
| Embeddings | Amazon Bedrock Titan Text v1 |
| LLM | Amazon Bedrock Nova Lite |
| Cloud | AWS us-east-1 |
| Language | Python 3.10+ |

---

## Quick Start

```bash
# Install
pip install langchain langchain-aws langchain-community langchain-text-splitters faiss-cpu boto3

# Run all 3 steps
python sebi_step1_generate_circulars.py
python sebi_step2_build_rag.py
python sebi_step3_chatbot.py
```

---

## Sample Questions

```
• What are SEBI rules on insider trading?
• What is the F&O margin requirement for stock futures?
• How should listed companies disclose material events?
• What are SEBI cybersecurity requirements for brokers?
• What is BRSR and who must file it?
• What are IPO lock-in requirements for promoters?
• How does SCORES 2.0 work?
• What is the minimum investment for PMS?
```

---

## How RAG Works

```
1. LOAD     → Read 10 circular text files
2. CHUNK    → Split into 800-char overlapping chunks (~120 total)
3. EMBED    → Convert each chunk to 1536-dim vector (Titan)
4. INDEX    → Store in FAISS for fast similarity search
5. QUERY    → Embed user question → find top 4 similar chunks
6. AUGMENT  → Build prompt with retrieved chunks as context
7. GENERATE → Nova Lite generates grounded answer + citations
```

---

## Why RAG vs Fine-tuning?

| | RAG | Fine-tuning |
|---|-----|------------|
| Update knowledge | Add new documents | Retrain model |
| Cost | Minimal | Expensive GPU |
| Transparency | Shows source chunks | Black box |
| Hallucination | Grounded in docs | Can hallucinate |
| **Best for** | **Regulatory Q&A** | Domain-specific tasks |

---

## TechM Agentic AI Portfolio

| Demo | Framework | Domain |
|------|-----------|--------|
| [Post-Market Surveillance](https://github.com/niranjanbits2/post-market-surveillance-agent) | Bedrock Agents | Medical Devices |
| [Contract Intelligence](https://github.com/niranjanbits2/contract-intelligence-agent) | Bedrock Agents | Legal/Banking |
| **SEBI Circular RAG** | **LangChain + FAISS** | **SEBI Regulations** |

---

**Tech Mahindra — Agentic AI Practice | April 2026**
