# RAG Chatbot using Ollama, ChromaDB and Streamlit

## Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot that answers questions from multiple PDF documents.

The chatbot:

- Extracts text from PDFs
- Uses OCR for scanned pages
- Splits documents into chunks
- Generates embeddings using BGE-M3
- Stores embeddings in ChromaDB
- Retrieves relevant chunks
- Uses Llama 3.2 through Ollama to generate answers
- Displays source PDF and page number

---

## Tech Stack

- Python
- Streamlit
- Ollama
- Llama 3.2
- BGE-M3
- ChromaDB
- LangChain Text Splitters
- PyMuPDF
- Tesseract OCR
