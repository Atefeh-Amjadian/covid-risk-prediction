# Explainable COVID-19 Risk Prediction

This project develops an explainable machine learning pipeline for predicting severe COVID-19 outcomes using real-world clinical data.

---

## 📌 Project Overview

Real-world clinical datasets are often incomplete, noisy, and difficult to use directly for machine learning.  
In this project, raw hospital-form data was transformed into structured clinical features such as symptoms, past medical history, COVID-related history, and vaccination status.

The main objective is to build an interpretable model that can predict the risk of severe COVID-19 outcomes (e.g., ICU admission) using only early-stage patient data.

---

## 🎯 Problem Statement

In clinical settings, early identification of high-risk COVID-19 patients is critical. However, available data is often:

- Incomplete (high missing values)
- Unstructured (form-based inputs)
- Inconsistent (mixed data types and formats)

This project addresses these challenges by designing a robust feature engineering pipeline and applying machine learning techniques for risk prediction.

---

## ⚙️ Key Contributions

- Reconstruction of structured data from semi-structured medical forms
- Feature engineering from real-world clinical records
- Handling high missingness and noisy data
- Prevention of data leakage (excluding post-treatment variables)
- Development of interpretable machine learning models
- Preparation of a reproducible and modular ML pipeline

---

## 🧠 Feature Engineering

The following feature groups were extracted and engineered:

### 1. Present Illness (Symptoms)
- Fever, Cough, Dyspnea, Anosmia, etc.
- Converted into binary clinical indicators

### 2. Past Medical History (PMH)
- Diabetes (Type 1 & 2), Hypertension, Heart Failure, Asthma, CKD, etc.

### 3. COVID-19 History
- Previous infection
- Hospitalization
- ICU admission
- Intubation

### 4. Vaccination
- Vaccinated (binary)
- Number of doses (numeric)

### 5. Clinical Examination
- Vital signs and clinical indicators (where available)

---

## ⚠️ Data Leakage Prevention

Treatment-related variables (e.g., medications such as antibiotics, antivirals, corticosteroids) were excluded from predictive modeling, as they represent post-diagnosis decisions and could introduce data leakage.

---

## 🔒 Data Privacy

The raw clinical dataset is not publicly shared due to privacy and data governance constraints.

This repository provides:
- The full preprocessing and feature engineering pipeline
- Model training and evaluation scripts

A synthetic or sample dataset may be added for demonstration purposes.

---

## 🏗️ Project Structure

covid-risk-prediction/
│
├── notebooks/
│   └── 01_exploration.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── features.py
│   ├── train.py
│   └── utils.py
│
├── data/
│   ├── raw/          # Not included (privacy)
│   ├── processed/
│   └── sample/
│
├── outputs/
│   ├── figures/
│   └── models/
│
├── requirements.txt
├── .gitignore
└── README.md

---

## 📊 Modeling Approach

Planned models include:
- Logistic Regression (baseline)
- Random Forest / XGBoost (main models)

Evaluation metrics:
- ROC-AUC
- Precision / Recall
- Confusion Matrix

---

## 🔍 Explainability

Model interpretability is a key focus of this project. Techniques such as:

- Feature importance
- SHAP (Shapley values)

will be used to understand model decisions and highlight clinically relevant predictors.

---

## 🚀 Current Status

- [x] Project structure initialized
- [x] Data privacy rules implemented
- [x] Exploratory data analysis (EDA)
- [x] Feature engineering (Symptoms, PMH, Vaccination, COVID History)
- [ ] Target variable definition
- [ ] Model training
- [ ] Model evaluation
- [ ] Explainability analysis

---

## 🧾 Resume Summary

Developed an explainable machine learning pipeline to predict severe COVID-19 outcomes using real-world clinical data with high missingness and noise.  
Engineered structured features from unstructured medical forms, handled data quality challenges, and ensured privacy compliance and prevention of data leakage.

---

## 💬 Motivation

This project demonstrates the ability to work with real-world healthcare data, handle complex preprocessing challenges, and build interpretable machine learning systems suitable for clinical decision support.

---

## 📫 Contact

For questions or collaboration, feel free to reach out.