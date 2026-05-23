# AI Document Assistant (RAG Based)

AI-powered Document Assistant built using FastAPI, LangChain, ChromaDB and OpenAI/Ollama.

The application allows users to upload PDF documents and ask contextual questions using Retrieval-Augmented Generation (RAG).

---

# Features

- PDF Upload Support
- Document Text Extraction
- Smart Text Chunking
- Embedding Generation
- Vector Database Storage
- RAG-based Question Answering
- Conversational Memory
- Source Citations
- FastAPI REST APIs
- Swagger API Documentation
- Docker Support
- Local LLM Support using Ollama

---

# Tech Stack

## Backend
- Python
- FastAPI

## AI / LLM
- LangChain
- OpenAI
- Ollama

## Vector Database
- ChromaDB

## Deployment
- Docker
- Docker Compose

---

# Project Structure

```bash
ai-document-assistant/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── utils/
│   └── main.py
│
├── data/
├── tests/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# System Architecture

1. User uploads PDF documents
2. PDF text is extracted
3. Text is split into chunks
4. Embeddings are generated
5. Embeddings stored in ChromaDB
6. User asks question
7. Relevant chunks retrieved
8. LLM generates contextual answer
9. Sources returned with response

---

# API Endpoints

## Health Check

```http
GET /health/
```

---

## Upload PDF

```http
POST /upload/
```

Upload one or more PDF files.

---

## Ask Questions

```http
POST /chat/
```

Example Request:

```json
{
  "question": "What is this document about?"
}
```

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/Mohit190/ai-document-assistant-rag.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_openai_key
MODEL_NAME=gpt-4o-mini
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

---

# Swagger Documentation

Open browser:

```txt
http://localhost:8000/docs
```

---

# Docker Setup

## Build and Run

```bash
docker compose up --build
```

---

# Ollama Local LLM Support

Install Ollama:

https://ollama.com

Run model:

```bash
ollama run llama3
```

Replace OpenAI model with Ollama in `llm_service.py`.

---

# Design Decisions

## Why FastAPI?
- Fast performance
- Easy API documentation
- Async support

## Why ChromaDB?
- Lightweight
- Easy local vector storage
- Good for small-medium RAG systems

## Why LangChain?
- Faster RAG pipeline development
- Easy retriever + memory integration

---

# Future Improvements

- Streaming responses
- Authentication & RBAC
- Hybrid search
- Reranking
- Multi-agent workflows using LangGraph
- PostgreSQL + pgvector
- CI/CD pipeline
- Unit testing

---

# Security Considerations

- API keys stored in `.env`
- `.env` excluded using `.gitignore`
- No secrets committed to repository

---

# Demo

Attached screenshots demonstrate:
- PDF upload
- API testing
- Question answering
- Source citations

---

# Author

Mohit Kumar
