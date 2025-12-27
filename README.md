# 🏦 Banking Churn Prediction Model
This project predicts whether a bank customer is likely to churn (leave the bank) based on customer demographic and account-related features.
It includes a trained machine learning model and a Streamlit web application for easy local deployment.

## 🚀 Features
Predicts customer churn (Yes / No)
Displays churn probability
Simple and interactive Streamlit web UI
Uses the same preprocessing pipeline as training (no mismatch)

## 🧠 Model Overview
Algorithm: Gradient Boosting (or your actual model)
Trained on historical bank customer data
Includes:
Label Encoding
One-Hot Encoding
Feature Scaling

## 📁 Project Structure
>     Banking-Churn-Prediction-Model/
      ├── app.py
      ├── gbm_churn_model.pkl
      ├── scaler.pkl
      ├── label_encoder_gender.pkl
      ├── feature_columns.pkl
      ├── README.md

## ⚙️ Installation
1️⃣ Prerequisites
Python 3.8+
pip (comes with Python)
Verify Python:
>     python --version

2️⃣ Install Required Libraries
>     pip install streamlit pandas scikit-learn joblib
Verify Streamlit: 
>     streamlit --version

## ▶️ Running the Application
### Option A: If you are using Jupyter Notebook 
Save all .pkl files and app.py
Open Anaconda Prompt
Navigate to the project folder: 
>     cd path\to\Banking-Churn-Prediction-Model
Run:
>     streamlit run app.py

### Option B: If you are running directly on a local machine (Windows)
Ensure Python and Streamlit are installed
Open CMD / PowerShell
Navigate to the project folder: 
>     cd path\to\Banking-Churn-Prediction-Model
Run: 
>     streamlit run app.py

## 🌐 Access the App
After running the command, a browser will open automatically.

## 🧪 Inputs Used for Prediction
Credit Score
Geography
Gender
Age
Tenure
Balance
Number of Products
Credit Card Availability
Active Member Status
Estimated Salary

## 👤 Author
### Muhammad Azeem
Machine Learning & Data Science Enthusiast

Any queries: muhammedazeemph15@gmail.com
