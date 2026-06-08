# Customer Churn Prediction

## Project Overview

This project predicts customer churn using Machine Learning and provides business insights through a Power BI dashboard and a Streamlit web application.

The objective is to identify customers who are likely to leave a telecom service provider and help businesses improve customer retention strategies.

---

## Dataset

* IBM Telco Customer Churn Dataset
* Total Records: 7,043 Customers
* Features: 45+

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Streamlit
* Power BI
* GitHub

---

## Data Preprocessing

* Missing Value Handling
* Feature Selection
* One-Hot Encoding
* SMOTE for Class Balancing
* Train-Test Split

---

## Machine Learning Models

### Logistic Regression

* Accuracy: 76.37%
* Precision: 53.78%
* Recall: 78.07%
* F1 Score: 63.69%

### Random Forest

* Accuracy: 95.17%
* Precision: 96.64%
* Recall: 84.76%
* F1 Score: 90.31%

### XGBoost (Best Model)

* Accuracy: 96.52%
* Precision: 96.83%
* Recall: 89.84%
* F1 Score: 93.20%
* ROC-AUC Score: 99.09%

---

## Key Business Insights

* Customers with lower satisfaction scores have the highest churn risk.
* Month-to-Month contracts contribute the largest share of churn.
* Fiber Optic internet users show relatively higher churn.
* Customers with longer tenure demonstrate stronger retention.
* Referral programs improve customer loyalty.
* Churned customers have lower overall lifetime value compared to retained customers.

---

## Power BI Dashboard

The dashboard provides:

* Churn Rate Analysis
* Contract Analysis
* Internet Type Analysis
* Customer Lifetime Value Analysis
* Satisfaction Score Analysis
* Interactive Slicers

### Dashboard Preview

![Dashboard](screenshots/dashboard.png)

---

## Streamlit Web Application

The application allows users to:

* Enter customer information
* Predict churn probability
* Identify customers at risk of leaving

### App Preview

![Streamlit App](screenshots/app.png)

---

## Project Structure

Customer-Churn-Prediction/

├── app.py

├── churn_model.pkl

├── model_columns.pkl

├── customer_churn_cleaned.csv

├── Customer_Churn_Prediction.ipynb

├── customer_churn_prediction.pbix

├── requirements.txt

├── README.md

└── screenshots/

    ├── app.png

    ├── dashboard.png

    └── model_result.png

---

## How to Run the Project

1. Clone the repository.
2. Install dependencies:

pip install -r requirements.txt

3. Run the Streamlit application:

streamlit run app.py

---

## Future Improvements

* Deploy the application on Streamlit Cloud.
* Add customer retention recommendations.
* Integrate real-time customer data.
* Improve model explainability using SHAP.

---

## Author

**Prasitha**

Customer Churn Prediction using XGBoost, Streamlit, and Power BI.
