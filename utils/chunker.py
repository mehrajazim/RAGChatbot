# utils/chunker.py
def chunk_text(text, chunk_size=512, overlap=256):
    """
    Splits text into overlapping chunks.
    - chunk_size: Maximum number of words per chunk.
    - overlap: Number of words to overlap between chunks.
    This overlap helps preserve context across boundaries.
    """
    words = text.split()
    chunks = []
    for start in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[start:start + chunk_size])
        chunks.append(chunk)
    return chunks
