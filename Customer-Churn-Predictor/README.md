Customer Churn Predictor
Overview

The Customer Churn Predictor is a Machine Learning application that predicts whether a customer is likely to leave a company based on customer demographics, account information, and usage patterns.

The project uses data preprocessing, feature engineering, and a classification model to identify customers at risk of churning. This can help businesses improve customer retention strategies and reduce revenue loss.

Features
Customer churn prediction using Machine Learning
Data preprocessing and feature engineering
Handling of categorical variables using one-hot encoding
Model training and evaluation
User-friendly prediction interface
End-to-end workflow from raw data to prediction
Dataset

The dataset contains customer-related information such as:

Credit Score
Geography
Gender
Age
Tenure
Balance
Number of Products
Credit Card Status
Active Member Status
Estimated Salary

Target Variable:

Exited (0 = Customer Stays, 1 = Customer Churns)
Project Structure
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
Technologies Used
Python
NumPy
Pandas
Scikit-learn
Matplotlib
Flask
HTML
CSS
Machine Learning Pipeline
Data Preprocessing
Handling irrelevant features
Encoding categorical variables
Feature scaling
Train-test split
Model Training

The model is trained on historical customer data to learn patterns associated with customer churn.

Algorithms commonly evaluated include:

Logistic Regression
Random Forest Classifier
Decision Tree Classifier
Gradient Boosting Classifier

The best-performing model is saved and used for prediction.

Installation
Clone the Repository
git clone https://github.com/AdityaRoy26/ML-Projects.git
Navigate to Project Directory
cd Customer-Churn-Predictor
Install Dependencies
pip install -r requirements.txt
Running the Application

Start the Flask application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000
Model Evaluation

Common evaluation metrics used:

Accuracy
Precision
Recall
F1 Score
Confusion Matrix

These metrics help assess how effectively the model identifies customers who are likely to churn.

Future Improvements
Deploy the application on Hugging Face Spaces
Add probability-based churn risk scores
Improve UI and user experience
Integrate advanced ensemble models
Add model explainability using SHAP or LIME
Use Cases
Customer Retention Analysis
Banking Customer Churn Prediction
Telecom Customer Churn Prediction
Subscription Service Analytics
Business Intelligence and Decision Support
Author

Aditya Roy

Machine Learning and Data Science Enthusiast

GitHub: AdityaRoy26 GitHub Profile

License

This project is intended for educational, learning, and portfolio purposes.
