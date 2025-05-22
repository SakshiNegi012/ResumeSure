from sentence_transformers import SentenceTransformer, util
import PyPDF2
import re

skills_list = [  
    'python', 'java', 'c++', 'machine learning', 'deep learning', 'data analysis', 'sql', 'flask', 'django'
]

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text.lower()

def calculate_ats_score(resume_text, jd_text):
    # Use BERT model for embeddings
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(resume_embedding, jd_embedding)
    return float(similarity[0][0]) * 100

def ats_analysis(resume_path, jd_path):
    resume_text = extract_text_from_pdf(resume_path)
    jd_text = extract_text_from_pdf(jd_path)

    ats_score = calculate_ats_score(resume_text, jd_text)

    return ats_score