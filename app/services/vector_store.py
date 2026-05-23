from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

DB_DIR = "chroma_db"

def store_documents(chunks):
    embeddings = OpenAIEmbeddings()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )

    vectordb.persist()

def get_vectorstore():
    embeddings = OpenAIEmbeddings()

    return Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings
    )