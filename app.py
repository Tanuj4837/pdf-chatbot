import streamlit as st
from utils import process_pdf, create_vector_store, get_answer

st.set_page_config(page_title="PDF Chatbot")

st.title("📄 LLM PDF Chatbot (RAG)")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    text_chunks = process_pdf(uploaded_file)
    vector_db = create_vector_store(text_chunks)

    st.success("PDF processed successfully!")

    query = st.text_input("Ask a question from the document:")

    if query:
        answer = get_answer(query, vector_db)
        st.subheader("Answer:")
        st.write(answer)
