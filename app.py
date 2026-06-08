import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model and columns
model = pickle.load(open("churn_model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

st.title("Customer Churn Prediction")

st.write("Enter customer details below:")

# Inputs
satisfaction_score = st.slider(
    "Satisfaction Score",
    1,
    5,
    3
)

tenure = st.number_input(
    "Tenure in Months",
    min_value=0,
    max_value=100,
    value=12
)

referrals = st.number_input(
    "Number of Referrals",
    min_value=0,
    max_value=20,
    value=0
)

dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    max_value=10,
    value=0
)

if st.button("Predict Churn"):

    # Create empty row with all 48 features
    input_data = pd.DataFrame(
        np.zeros((1, len(model_columns))),
        columns=model_columns
    )

    # Fill important features
    input_data["Satisfaction Score"] = satisfaction_score
    input_data["Tenure in Months"] = tenure
    input_data["Number of Referrals"] = referrals
    input_data["Number of Dependents"] = dependents

    # Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    if prediction == 1:
        st.error(
            f"⚠ Customer likely to churn\n\nProbability: {probability:.2f}%"
        )
    else:
        st.success(
            f"✅ Customer likely to stay\n\nProbability of churn: {probability:.2f}%"
        )