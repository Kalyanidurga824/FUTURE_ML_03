import streamlit as st
import joblib
import os
import fitz  # PyMuPDF
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# File Paths
# -------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "tfidf_vectorizer.pkl"
)

# -------------------------------
# Load TF-IDF Vectorizer
# -------------------------------

tfidf = joblib.load(MODEL_PATH)

# -------------------------------
# Function to Extract PDF Text
# -------------------------------

def extract_text_from_pdf(pdf_file):
    text = ""

    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text


# -------------------------------
# Streamlit App
# -------------------------------

st.title("🤖 AI Resume Screening System")

st.write(
    "Upload candidate resumes and compare them with the Job Description."
)

# -------------------------------
# Job Description
# -------------------------------

job_description = st.text_area(
    "Enter Job Description"
)

# -------------------------------
# Resume Upload
# -------------------------------

uploaded_files = st.file_uploader(
    "Upload Candidate Resumes (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

# -------------------------------
# Rank Button
# -------------------------------

if st.button("Rank Candidates"):

    if job_description.strip() == "":
        st.warning("Please enter a Job Description.")

    elif not uploaded_files:
        st.warning("Please upload at least one resume.")

    else:

        resumes = []

        for file in uploaded_files:

            resume_text = extract_text_from_pdf(file)

            resumes.append({
                "Candidate": file.name,
                "Resume": resume_text
            })

        df = pd.DataFrame(resumes)

        # -------------------------------
        # Convert text to TF-IDF vectors
        # -------------------------------

        job_vector = tfidf.transform([job_description])

        resume_vectors = tfidf.transform(df["Resume"])

        # -------------------------------
        # Calculate Cosine Similarity
        # -------------------------------

        similarity = cosine_similarity(
            resume_vectors,
            job_vector
        )

        df["Match Score"] = similarity.flatten()

        # -------------------------------
        # Sort Candidates by Match Score
        # -------------------------------

        df = df.sort_values(
            by="Match Score",
            ascending=False
        ).reset_index(drop=True)

        # -------------------------------
        # Add Rank Column
        # -------------------------------

        df.insert(0, "Rank", range(1, len(df) + 1))

        # -------------------------------
        # Convert Score to Percentage
        # -------------------------------

        df["Match Score"] = (df["Match Score"] * 100).round(2)

        # -------------------------------
        # Display Results
        # -------------------------------

        st.success("✅ Ranking Completed!")

        st.subheader("🏆 Candidate Rankings")

        st.dataframe(
            df[["Rank", "Candidate", "Match Score"]],
            use_container_width=True,
            hide_index=True
        )

        # -------------------------------
        # Best Candidate
        # -------------------------------

        st.subheader("🥇 Best Matching Candidate")

        st.success(
            f"**{df.iloc[0]['Candidate']}** "
            f"matched **{df.iloc[0]['Match Score']}%** with the Job Description."
        )

        # -------------------------------
        # Bar Chart
        # -------------------------------

        st.subheader("📊 Match Score Comparison")

        chart_df = df.set_index("Candidate")[["Match Score"]]

        st.bar_chart(chart_df)