# Bangalore House Price Predictor

## Overview

The Bangalore House Price Predictor is a Machine Learning web application that estimates house prices in Bangalore based on property features such as location, total square footage, number of bathrooms, and BHK configuration.

The project uses data preprocessing, feature engineering, and a Ridge Regression model to predict house prices and provides a simple web interface built with Flask.

---

## Features

- Predicts house prices in Bangalore
- Location-based price estimation
- User-friendly Flask web interface
- Trained Ridge Regression model
- Real-time predictions from user input

---

## Tech Stack

### Machine Learning
- Python
- NumPy
- Pandas
- Scikit-learn

### Web Development
- Flask
- HTML
- CSS

### Model
- Ridge Regression

---

## Project Structure

```text
Bangalore-House-Price-Predictor
│
├── app.py
├── Ridge.pkl
├── Cleaned_data.csv
├── Bang-HousepricePred.ipynb
├── requirements.txt
├── README.md
│
├── templates
│   └── index.html
│
└── .gitignore
```

---

## Dataset Features

The model uses the following input features:

| Feature | Description |
|----------|-------------|
| location | Area where the property is located |
| total_sqft | Total area of the property in square feet |
| bath | Number of bathrooms |
| bhk | Number of bedrooms |

Target Variable:

- price

---

## Model Training Workflow

1. Data Cleaning
2. Handling Missing Values
3. Feature Engineering
4. Outlier Removal
5. Categorical Encoding
6. Train-Test Split
7. Ridge Regression Model Training
8. Model Serialization using Pickle

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/AdityaRoy26/ML-Projects.git
```

### Navigate to the Project Folder

```bash
cd Bangalore-House-Price-Predictor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
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

## Example Input

| Feature | Value |
|----------|--------|
| Location | Whitefield |
| Total Sqft | 1200 |
| Bathrooms | 2 |
| BHK | 2 |

Output:

```text
Estimated House Price: ₹ XX Lakhs
```

---

## Future Improvements

- Enhanced UI design
- Interactive visualizations
- Support for additional property features
- Model comparison and tuning
- Cloud deployment

---

## Author

Aditya Roy

GitHub: https://github.com/AdityaRoy26
