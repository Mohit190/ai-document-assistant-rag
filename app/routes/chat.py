from fastapi import APIRouter
from pydantic import BaseModel

from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

from app.services.vector_store import get_vectorstore

router = APIRouter()

memory_store = []

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(request: ChatRequest):

    vectordb = get_vectorstore()

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(model="gpt-3.5-turbo")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    answer = qa_chain.run(request.question)

    memory_store.append({
        "question": request.question,
        "answer": answer
    })

    return {
        "question": request.question,
        "answer": answer,
        "memory": memory_store[-5:]
    }