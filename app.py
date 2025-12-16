import streamlit as st
import pandas as pd
import joblib

# Load artifacts
model = joblib.load('gbm_churn_model.pkl')
scaler = joblib.load('scaler.pkl')
le_gender = joblib.load('label_encoder_gender.pkl')
feature_columns = joblib.load('feature_columns.pkl')

st.title("Customer Churn Prediction")

credit_score = st.slider("Credit Score", 300, 850, 650)
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 100, 40)
tenure = st.slider("Tenure", 0, 10, 3)
balance = st.number_input("Balance", 0.0, 300000.0, 60000.0)
num_products = st.slider("Number of Products", 1, 4, 2)
has_card = st.selectbox("Has Credit Card", [0, 1])
is_active = st.selectbox("Is Active Member", [0, 1])
salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

if st.button("Predict"):
    df = pd.DataFrame([{
        'CreditScore': credit_score,
        'Geography': geography,
        'Gender': gender,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_products,
        'HasCrCard': has_card,
        'IsActiveMember': is_active,
        'EstimatedSalary': salary
    }])

    df['Gender'] = le_gender.transform(df['Gender'])
    df = pd.get_dummies(df, columns=['Geography'], drop_first=True)
    df = df.reindex(columns=feature_columns, fill_value=0)
    df_scaled = scaler.transform(df)

    pred = model.predict(df_scaled)[0]
    prob = model.predict_proba(df_scaled)[0][1]

    st.success(f"Prediction: {'Churn' if pred else 'No Churn'}")
    st.info(f"Churn Probability: {prob:.2%}")
    