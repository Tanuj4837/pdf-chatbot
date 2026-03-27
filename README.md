# RAG Chatbot to chat with PDFs using Gemini

This project is a web application that leverages advanced AI models to perform Question Answering (QA) from PDF documents. It uses Retrieval-Augmented Generation (RAG) techniques to provide accurate and context-aware answers to user queries based on the content of the uploaded PDF files.

## Features

- **PDF Text Extraction**: Extract text from multiple PDF documents.
- **Text Chunking**: Split the extracted text into manageable chunks for processing.
- **Google Generative AI Embeddings**: Create vector representations of text chunks using Google's advanced AI models.
- **FAISS Vector Store**: Utilize FAISS for efficient similarity search among text chunks.
- **Conversational QA Chain**: Integrate Google's Gemini model to provide detailed and context-aware answers to user questions.
- **Streamlit Interface**: A user-friendly interface to upload PDFs and ask questions interactively.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Sahiltr/qa-with-pdf-using-gemini.git
    cd qa-with-pdf-using-gemini
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Google API key by creating a `.env` file in the project directory:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Use the interface to upload PDF files and ask questions based on the content of those files.

## Project Structure

- `app.py`: The main script for running the Streamlit application.
- `requirements.txt`: The list of required Python packages.
- `.env`: Environment variables file containing your Google API key.

## Example

Upload one or more PDF files using the sidebar, then enter your question in the text input box. The application will process the PDFs, create text chunks, generate embeddings, and provide a detailed answer based on the context found in the documents.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any features, bug fixes, or enhancements.


