# Pharma Knowledge Assistant

An AI-powered pharmaceutical knowledge assistant built using FastAPI, React, ChromaDB, and Ollama.

## Overview

Pharma Knowledge Assistant enables users to upload pharmaceutical documents and ask natural language questions. The system retrieves relevant information using Retrieval-Augmented Generation (RAG) and generates context-aware responses with source citations.

---

## Features

* PDF document upload and ingestion
* Semantic search using ChromaDB
* Retrieval-Augmented Generation (RAG)
* Ollama-powered LLM responses
* Source citation with page numbers
* Intent classification

  * Greeting detection
  * Short/Vague query handling
  * Out-of-scope detection
* Conversation memory with session management
* React-based chat interface
* Auto-generated session IDs

---

## Tech Stack

### Backend

* FastAPI
* Python
* ChromaDB
* LangChain
* Ollama
* Sentence Transformers
* PyPDF

### Frontend

* React
* Vite
* Axios

---

## Architecture

User Query → Intent Classification → Tool Selection → RAG Retrieval → LLM Generation → Response with Sources

---

## Project Structure

```text
app/
    api/
    services/
    db/

frontend/
    src/
        components/
        services/
```

---

## How to Run

### Backend

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Sample Questions

* What is Brintellix used for?
* What are the adverse reactions of Brintellix?
* What is the active ingredient in Brintellix?

---

## Future Enhancements

* Multi-document support
* Streaming responses
* Docker deployment
* Cloud deployment
* Authentication
* Advanced memory management

