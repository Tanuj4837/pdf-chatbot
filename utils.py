from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import OpenAI

import os

# --- Extract + split text ---
def process_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)
    return chunks


# --- Create vector store ---
def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings()
    vector_db = FAISS.from_texts(chunks, embeddings)
    return vector_db


# --- Query + Answer ---
def get_answer(query, vector_db):
    docs = vector_db.similarity_search(query)

    context = " ".join([doc.page_content for doc in docs])

    # Simple LLM response (replace API key if needed)
    try:
        llm = OpenAI()
        response = llm(f"Answer based on context:\n{context}\n\nQuestion: {query}")
        return response
    except:
        return "LLM API not configured. Showing retrieved context:\n" + context
