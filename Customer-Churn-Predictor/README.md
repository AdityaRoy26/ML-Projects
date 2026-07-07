# Customer Churn Predictor

## Overview

The Customer Churn Predictor is a Machine Learning application that predicts whether a customer is likely to leave a company based on customer demographics, account information, and financial attributes.

Customer churn is a critical business problem because retaining existing customers is often more cost-effective than acquiring new ones. This project leverages Machine Learning techniques to identify customers at risk of churning, enabling businesses to take proactive retention measures.

---

## Features

- Predicts customer churn using Machine Learning
- Data preprocessing and feature engineering
- Categorical variable encoding
- Feature scaling and model training
- Interactive web interface using Flask
- Real-time churn prediction
- End-to-end machine learning workflow

---

## Dataset

The dataset contains customer information including:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary

### Target Variable

- Exited
  - 0 → Customer Stays
  - 1 → Customer Churns

---

## Project Structure

```text
Customer-Churn-Predictor/
│
├── app.py
├── churn_model.pkl
├── customer_churn.ipynb
├── requirements.txt
├── README.md
│
├── data/
│   └── Churn_Modelling.csv
│
├── templates/
│   └── index.html
│
└── static/
```

---

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Flask
- HTML
- CSS

---

## Machine Learning Pipeline

### 1. Data Preprocessing

- Removed unnecessary columns
- Handled categorical features
- Applied One-Hot Encoding
- Performed feature scaling

### 2. Model Training

The dataset was split into training and testing sets to build a classification model capable of predicting customer churn.

### 3. Model Evaluation

The model was evaluated using multiple performance metrics to ensure reliable predictions.

### 4. Deployment

The trained model was integrated into a Flask web application for real-time predictions.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/AdityaRoy26/ML-Projects.git
```

### Navigate to the Project Directory

```bash
cd Customer-Churn-Predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Model Evaluation Metrics

The model performance can be evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

These metrics help determine how effectively the model identifies customers likely to churn.

---

## Use Cases

- Banking Customer Retention
- Telecom Customer Churn Prediction
- Subscription-Based Businesses
- Customer Retention Analysis
- Business Intelligence Applications

---

## Future Enhancements

- Deploy on Hugging Face Spaces
- Add churn probability scores
- Improve user interface
- Implement advanced ensemble models
- Add model explainability using SHAP

---

## Author

Aditya Roy

GitHub: https://github.com/AdityaRoy26

---

## License

This project is intended for educational, learning, and portfolio purposes.
