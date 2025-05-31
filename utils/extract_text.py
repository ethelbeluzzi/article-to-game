import fitz  # PyMuPDF
import docx
from newspaper import Article
import tempfile
import os

def extract_text_from_input(uploaded_file, url):
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            return extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            return extract_text_from_docx(uploaded_file)
    elif url:
        return extract_text_from_url(url)
    return None

def extract_text_from_pdf(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file.read())
        tmp_path = tmp_file.name

    doc = fitz.open(tmp_path)
    texto = ""
    for page in doc:
        texto += page.get_text()
    doc.close()

    os.remove(tmp_path)
    return texto.strip()

def extract_text_from_docx(file):
    doc = docx.Document(file)
    texto = "\n".join([p.text for p in doc.paragraphs if p.text.strip() != ""])
    return texto.strip()

def extract_text_from_url(url):
    article = Article(url)
    try:
        article.download()
        article.parse()
        return article.text.strip()
    except:
        return None
