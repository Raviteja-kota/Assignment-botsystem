# AI Cognitive Routing & RAG System

## Overview
This project implements a cognitive AI loop with:
- Vector-based persona routing
- Autonomous content generation
- RAG-based argument defense

---

## Phase 1: Vector Routing
- Used SentenceTransformers + FAISS
- Semantic similarity instead of keyword matching
- Bots selected using cosine similarity threshold

---

## Phase 2: LangGraph Workflow
Nodes:
1. Decide Topic
2. Search (mock tool)
3. Draft Post

Output is strict JSON format.

---

## Phase 3: RAG Defense
- Full conversation context provided
- System-level prompt prevents prompt injection
- Bot maintains persona even under attack

---

## How to Run

pip install -r requirements.txt

python phase1_router.py
python phase2_langgraph.py
python phase3_rag.py
