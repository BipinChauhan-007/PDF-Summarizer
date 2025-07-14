# backend/utils.py
import pdfplumber

def extract_text(file):
    if file.name.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file.name.endswith('.txt'):
        return file.read().decode("utf-8")
    return ""
