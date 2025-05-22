import docx2txt
import PyPDF2
import re

def extract_text(file_path):
    """
    Extracts and preprocesses text from a PDF or DOCX file.
    """
    text = ''
    if file_path.lower().endswith('.pdf'):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    elif file_path.lower().endswith('.docx'):
        text = docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")
    
    return preprocess_text(text)

def preprocess_text(text):
    """
    Lowercases, removes extra whitespace and punctuation from text.
    """
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)            # Remove extra whitespace
    text = re.sub(r'[^\w\s]', '', text)         # Remove punctuation
    return text.strip()