# RAG Chatbot with FastAPI, Gemini API, and Pinecone

This project implements a Retrieval-Augmented Generation (RAG) chatbot using an MVC (Model-View-Controller) design pattern. The chatbot is built with FastAPI and leverages the Gemini API for natural language generation along with Pinecone for vector storage and retrieval. The project also uses the `all-MiniLM-L6-v2` model from SentenceTransformers for creating text embeddings.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)

## Overview

The RAG Chatbot allows users to:
- Upload PDF files through a browser interface.
- Extract and chunk text from PDFs.
- Store text embeddings in a Pinecone index.
- Ask questions that are answered using context retrieved from the stored PDF chunks.
- Generate responses with the Gemini API based on the retrieved context.

## Architecture

This project follows the **MVC pattern**:
- **Model**: Responsible for data processing, including PDF text extraction, text chunking, and generating embeddings using `all-MiniLM-L6-v2`.
- **View**: Provides the HTML interface using FastAPI's templating engine. Static files (CSS, JS) are served from a designated folder.
- **Controller**: Contains the business logic for processing file uploads and handling query requests. It routes requests to the correct model functions and then returns the generated response.

## Tech Stack

- **FastAPI**: Web framework to build the API.
- **Uvicorn**: ASGI server to run the FastAPI application.
- **Google Gemini API**: Generates responses based on the provided prompt.
- **Pinecone**: A vector database for storing and retrieving text embeddings.
- **SentenceTransformers (all-MiniLM-L6-v2)**: Generates text embeddings that balance speed and semantic quality.
- **PyMuPDF (fitz)**: Extracts text from PDF documents.
- **Python-dotenv**: Loads environment variables from a `.env` file.

## Setup and Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/mehrajazim/RAGChatbot.git
cd RAG_CHATBOT_MVC
```
2.  **Create and Activate a Virtual Environment**
    
```bash
python -m venv venv
```
On mac/Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```
3.  **Install Dependencies:**
```bash
pip install -r requirements.txt
```
4.  **Set Environment Variables:**
```python
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_ENV=us-east-1
PINECONE_INDEX=your-index-name
GENAI_API_KEY=your-gemini-api-key
```
5. **Verify the Configuration**

```python
import os
from dotenv import load_dotenv

load_dotenv()

print("Pinecone API Key:", os.getenv("PINECONE_API_KEY"))
print("Pinecone Env:", os.getenv("PINECONE_ENV"))
print("Pinecone Index:", os.getenv("PINECONE_INDEX"))
print("Gemini API Key:", os.getenv("GENAI_API_KEY"))
```
6. **Start the Application**
```bash
uvicorn app:app --reload
```
After the server starts, you can access the API documentation at http://127.0.0.1:8000/docs and the web interface at http://127.0.0.1:8000/.
