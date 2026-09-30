# Student Performance Prediction 🎓

A Machine Learning project that predicts a student's total score based on their study habits, attendance, and class participation.

## 📌 Project Overview

The goal of this project is to predict a student's total score using three main factors:

- Weekly Self Study Hours
- Attendance Percentage
- Class Participation

I trained and compared two Machine Learning regression models and then used the Random Forest model in a Streamlit web application.

## 📊 Features Used

| Feature | Description |
|---|---|
| `weekly_self_study_hours` | Number of hours spent studying per week |
| `attendance_percentage` | Student's attendance percentage |
| `class_participation` | Student's participation percentage |

### Target

`total_score`

## 🤖 Machine Learning Models

### 1. Linear Regression

Used as a baseline regression model.

### 2. Random Forest Regressor

Trained and evaluated on the same test data.

## 📈 Model Evaluation

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

| Model | MAE | MSE | R² |
|---|---:|---:|---:|
| Linear Regression | 7.16 | 80.94 | 0.660 |
| Random Forest | 6.10 | 67.26 | 0.717 |

Based on the held-out test set, Random Forest produced lower MAE and MSE and a higher R² score, so it was selected for the Streamlit application.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Google Colab
- Jupyter Notebook

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Understanding & Cleaning
   ↓
Feature Selection
   ↓
Train / Test Split
   ↓
Linear Regression
   ↓
Random Forest
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Streamlit Application
