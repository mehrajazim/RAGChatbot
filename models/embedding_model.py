# models/embedding_model.py
from sentence_transformers import SentenceTransformer
from config import index

# Using "all-MiniLM-L6-v2" because it balances speed and semantic quality for retrieval tasks.
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    """Generates an embedding for a given text."""
    return embedding_model.encode(text).tolist()

def store_chunks(chunks):
    """
    Stores each text chunk in Pinecone with its embedding.
    Each chunk is assigned a unique ID.
    """
    vectors = []
    for i, chunk in enumerate(chunks):
        vector = get_embedding(chunk)
        # Create a unique ID for each chunk.
        vector_id = f"chunk_{i}"
        vectors.append((vector_id, vector, {"text": chunk}))
    # Upsert vectors in batch into Pinecone.
    index.upsert(vectors)

def query_chunks(query, top_k=3):
    """
    Retrieves the top_k relevant text chunks from Pinecone for the given query.
    Returns: A concatenated string of retrieved text.
    """
    query_vector = get_embedding(query)
    results = index.query(vector=query_vector, top_k=top_k, include_metadata=True)
    # Join the text from each matching chunk.
    return "\n".join([match["metadata"]["text"] for match in results["matches"]])
