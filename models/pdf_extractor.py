# models/pdf_extractor.py
import fitz  # PyMuPDF

def extract_text_from_pdf(file_obj):
    """
    Extracts text from a PDF file.
    file_obj: A file-like object.
    Returns: The full text as a string.
    """
    # Open the PDF from the byte stream and extract text from each page.
    doc = fitz.open(stream=file_obj.read(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in doc])
    return text
