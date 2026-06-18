<<<<<<< HEAD
# 🤖 AI Resume Screening System

## 📌 Project Overview

The **AI Resume Screening System** is a Machine Learning-based web application that automates the resume screening process using **Natural Language Processing (NLP)** techniques.

The system analyzes candidate resumes, compares them with job descriptions, and identifies the most suitable candidates based on their matching score.

Traditional resume screening requires significant manual effort and time. This project provides an automated solution that helps recruiters quickly filter candidates, improve hiring efficiency, and make data-driven decisions.

The project includes an interactive **Streamlit Web Application** where users can enter job requirements and analyze resumes through a simple and user-friendly interface.

---

# 🎯 Objectives

- Automate the resume screening process
- Reduce manual effort in candidate filtering
- Match candidate skills with job requirements
- Rank resumes based on relevance score
- Provide a simple AI-powered recruitment solution

---

# 📂 Dataset

**Resume Dataset (Kaggle)**

The dataset contains resume text data used for NLP processing and developing the resume matching system.

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Machine Learning & NLP

- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Text Feature Extraction

## Libraries & Frameworks

- Pandas
- NumPy
- NLTK
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn

## Development Tools

- Jupyter Notebook
- VS Code
- Git & GitHub

---

# 🔄 Project Workflow

```
Resume Dataset
        |
        ↓
Data Preprocessing
        |
        ↓
Text Cleaning
        |
        ↓
Tokenization & Stopword Removal
        |
        ↓
TF-IDF Vectorization
        |
        ↓
Feature Extraction
        |
        ↓
Cosine Similarity Calculation
        |
        ↓
Resume Matching Score
        |
        ↓
Candidate Ranking
        |
        ↓
Streamlit Web Application
```

---

# ✨ Features

✅ Automated Resume Screening  
✅ Resume and Job Description Matching  
✅ Candidate Ranking System  
✅ NLP-based Text Processing  
✅ TF-IDF Feature Extraction  
✅ Cosine Similarity-based Matching  
✅ Fast Resume Analysis  
✅ Interactive Web Interface using Streamlit  

---

# 🧠 Machine Learning Model

## TF-IDF Vectorizer + Cosine Similarity

The system converts resume content and job descriptions into numerical vectors using **TF-IDF Vectorization**.

Cosine Similarity is then applied to calculate the similarity between resumes and job requirements.

Higher similarity scores indicate better candidate-job matching.

---

# 🌐 Web Application

The project contains an interactive **Streamlit Web Application** that allows users to perform AI-based resume screening.

## Web Application Features

- Enter job description
- Analyze resume content
- Process text automatically
- Calculate matching percentage
- Display candidate suitability results

## Run Web Application

```bash
streamlit run app/app.py
```

## Application URL

```
Local URL:
http://localhost:8501
```

```
Network URL:
http://<your-network-ip>:8501
```

---

# ⚙️ Installation & Setup

## Step 1: Clone Repository

```bash
git clone <repository-url>
```

## Step 2: Navigate to Project Folder

```bash
cd AI_Resume_Screening_System
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run Application

```bash
streamlit run app/app.py
```

---

# 📁 Project Structure

```
AI_Resume_Screening_System/
│
├── app/
│   └── app.py                         # Streamlit Web Application
│
├── data/
│   └── resume_dataset.csv             # Resume Dataset
│
├── models/
│   └── tfidf_vectorizer.pkl           # TF-IDF Model
│
├── notebook/
│   └── Resume_Screening.ipynb         # Model Development Notebook
│
├── requirements.txt                   # Required Dependencies
│
├── README.md                          # Project Documentation
│
├── LICENSE                            # License File
│
└── .gitignore                         # Git Ignore File
```

---

# 📊 Applications

- AI-powered recruitment systems
- Applicant Tracking Systems (ATS)
- HR automation platforms
- Internship candidate screening
- Job recommendation systems
- Skill-based candidate matching

---

# 🚀 Future Improvements

- Support PDF and DOCX resume uploads
- Implement Deep Learning models like BERT/LSTM
- Advanced skill extraction
- Candidate experience analysis
- Resume analytics dashboard
- Database integration
- Cloud deployment
- Integration with recruitment platforms

---
=======
# FUTURE_ML_03
AI Resume Screening System is a Machine Learning and NLP-based application that automates resume analysis and candidate ranking. It uses TF-IDF Vectorization and Cosine Similarity to match resumes with job descriptions. Built with Python and Streamlit, it provides an interactive web interface for efficient AI-powered recruitment screening.
>>>>>>> befd03c6a0f224a8c44b78157c1560157949156f
