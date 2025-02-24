# controllers/chat_controller.py
from fastapi import APIRouter, Form
from models.embedding_model import query_chunks
import google.generativeai as genai

router = APIRouter()

@router.post("/ask")
async def ask_question(question: str = Form(...)):
    """
    Endpoint for answering a question.
    It retrieves relevant context from Pinecone and uses Gemini API to generate an answer.
    """
    # Retrieve relevant text from stored PDF chunks.
    context = query_chunks(question)
    # Create a prompt that combines the retrieved context and the user’s question.
    # prompt = f"Based on the following context, answer the question.\n\nContext:\n{context}\n\nQuestion: {question}"
    # Call the Gemini API for the answer.
    prompt = f"""
Answer the question using ONLY this context:
---
{context}
---
If the answer isn't in the context, say "I don't know".

Question: {question}
"""
    
    
    
    model=genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)  #genai.chat(model="gemini-pro", messages=[{"role": "user", "content": prompt}])
    return {"answer": response.text}
    # print(response.text)
