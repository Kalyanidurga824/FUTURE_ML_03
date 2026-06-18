import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import os


# -------------------------------
# File Paths
# -------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "tfidf_vectorizer.pkl"
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "ranked_candidates.csv"
)


# -------------------------------
# Load Model and Data
# -------------------------------

tfidf = joblib.load(MODEL_PATH)

df = pd.read_csv(DATA_PATH)


# -------------------------------
# App Title
# -------------------------------

st.title("🤖 AI Resume Screening System")

st.write(
    "NLP based resume screening and candidate ranking system"
)


# -------------------------------
# Job Description Input
# -------------------------------

job_description = st.text_area(
    "Enter Job Description"
)


# -------------------------------
# Rank Candidates
# -------------------------------

if st.button("Rank Candidates"):

    if job_description.strip() == "":

        st.warning(
            "Please enter a job description"
        )

    else:

        # Convert job description into vector

        job_vector = tfidf.transform(
            [job_description]
        )


        # Convert resumes into vectors

        resume_vectors = tfidf.transform(
            df["clean_resume"]
        )


        # Calculate similarity

        scores = cosine_similarity(
            resume_vectors,
            job_vector
        )


        df["match_score"] = scores.flatten()


        # Sort candidates

        result = df.sort_values(
            by="match_score",
            ascending=False
        )


        st.subheader(
            "🏆 Top Candidates"
        )


        # Display result

        display_columns = [
            "ID",
            "Category",
            "match_score",
            "skills",
            "missing_skills"
        ]


        available_columns = [
            col for col in display_columns
            if col in result.columns
        ]


        st.dataframe(
            result[available_columns].head(10),
            use_container_width=True
        )


        # Chart

        st.subheader(
            "📊 Candidate Ranking Score"
        )


        chart = result.head(10)


        st.bar_chart(
            chart.set_index("Category")
            ["match_score"]
        )