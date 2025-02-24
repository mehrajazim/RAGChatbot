
import google.generativeai as genai
import os
from dotenv import load_dotenv
from pinecone import Pinecone
load_dotenv()


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
pc = Pinecone(api_key=PINECONE_API_KEY)

if PINECONE_INDEX not in pc.list_indexes().names():
    print(f"Index '{PINECONE_INDEX}' not found.")
else:
    index = pc.Index(PINECONE_INDEX)

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
