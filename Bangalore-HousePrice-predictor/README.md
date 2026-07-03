# Bangalore House Price Predictor

## Live Demo

Hugging Face Deployment:

https://huggingface.co/spaces/AdityaRoy2026/Bangalore-HousePrice-Predictor

---

## Overview

The Bangalore House Price Predictor is an end-to-end Machine Learning project that estimates residential property prices in Bangalore based on key property features such as location, total square footage, number of bathrooms, and BHK configuration.

The project covers the complete machine learning workflow including data cleaning, feature engineering, model training, model evaluation, deployment, and web application development.

The final application is deployed on Hugging Face Spaces and provides real-time house price predictions through a simple web interface.

---

## Features

- Real-time Bangalore house price prediction
- Location-based property valuation
- Interactive web interface built with Flask
- Ridge Regression model for prediction
- End-to-end deployment on Hugging Face Spaces
- Clean and responsive user experience

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

### Deployment

- Hugging Face Spaces
- Docker

---

## Model Information

### Algorithm

- Ridge Regression

### Input Features

| Feature | Description |
|----------|-------------|
| location | Property location in Bangalore |
| total_sqft | Total area in square feet |
| bath | Number of bathrooms |
| bhk | Number of bedrooms |

### Target Variable

- price

---

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Missing Value Handling
4. Feature Engineering
5. Outlier Detection and Removal
6. Categorical Encoding
7. Model Training
8. Model Evaluation
9. Model Serialization using Pickle
10. Flask Application Development
11. Docker Containerization
12. Deployment on Hugging Face Spaces

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
├── Dockerfile
├── README.md
│
├── templates
│   └── index.html
│
└── .gitignore
```

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

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

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

## Running Locally

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Example Prediction

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

## Deployment

The application is deployed on Hugging Face Spaces using Docker.

Live Application:

https://huggingface.co/spaces/AdityaRoy2026/Bangalore-HousePrice-Predictor

---

## Future Improvements

- Improved UI/UX design
- Additional property features
- Advanced ensemble models
- Interactive visualizations
- Model monitoring and retraining pipeline
- Comparative model evaluation dashboard

---

## Author

Aditya Roy

GitHub: https://github.com/AdityaRoy26

Hugging Face: https://huggingface.co/AdityaRoy2026
