from ats_with_skills import ats_analysis, extract_text_from_pdf
from company_recommendation import recommend_companies

# 🔁 Update paths to your actual files
resume_path = "resume.pdf"
jd_path = "job_description.pdf"
dataset_path = "expanded_tech_resume_job_dataset.csv"

# Step 1: Calculate ATS score only (assuming ats_analysis still returns these)
ats_score = ats_analysis(resume_path, jd_path)  # ignore matched_skills and missing_skills

# Step 2: Extract text from resume and JD PDFs
resume_text = extract_text_from_pdf(resume_path)
jd_text = extract_text_from_pdf(jd_path)

# Step 3: Get company recommendations based on resume and JD
recommended_companies = recommend_companies(resume_text, jd_text, dataset_path)

# ✅ Output results
print(f"\n🎯 ATS Score: {ats_score:.2f}%\n")

# Removed printing of skills matched and missing completely

print("\n🏢 Recommended Companies:")
for company in recommended_companies:
    print(f"{company['Company_Name']} - {company['Job_Role']} ({company['Similarity_Score']:.2f}%)")
