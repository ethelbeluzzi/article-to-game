import fitz  # PyMuPDF
import docx
import tempfile
import os

def extract_text_from_input(uploaded_file):
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            return extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            return extract_text_from_docx(uploaded_file)
    return None

def extract_text_from_pdf(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file.read())
        tmp_path = tmp_file.name

    texto = ""
    try:
        doc = fitz.open(tmp_path)
        for page in doc:
            texto += page.get_text()
        doc.close()
    except Exception:
        texto = ""
    finally:
        os.remove(tmp_path)

    return texto.strip()

def extract_text_from_docx(file):
    try:
        doc = docx.Document(file)
        texto = "\n".join([p.text for p in doc.paragraphs if p.text.strip() != ""])
        return texto.strip()
    except Exception:
        return ""
