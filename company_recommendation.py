import pandas as pd
from sentence_transformers import SentenceTransformer, util

def recommend_companies(resume_text, jd_text, dataset_path, top_k=5):
    
    df = pd.read_csv(dataset_path)
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    combined_input = resume_text + " " + jd_text
    input_embedding = model.encode(combined_input, convert_to_tensor=True)

    df['Combined'] = df['Resume_Text'] + " " + df['Job_Description']
    company_embeddings = model.encode(df['Combined'].tolist(), convert_to_tensor=True)
  
    similarities = util.pytorch_cos_sim(input_embedding, company_embeddings)[0]
    top_results = similarities.topk(k=top_k)
    recommended = []
    for score, idx in zip(top_results.values, top_results.indices):
        idx = int(idx)
        recommended.append({
            'company': df.iloc[idx]['Company_Name'],
            'role': df.iloc[idx]['Role'],
            'percentage': round(float(score) * 100, 2)
        })

    return recommended