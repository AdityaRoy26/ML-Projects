# SMS Spam Classifier

A machine learning model that classifies SMS messages as spam or legitimate (ham). The model is trained on a labeled dataset of text messages and served through a lightweight web interface built with Streamlit.

## How It Works

The classifier uses a text vectorization pipeline followed by a supervised classification model. Raw SMS text is preprocessed and converted into numerical features using a TF-IDF vectorizer, which are then passed to a trained classifier to predict whether the message is spam or ham. Both the vectorizer and model are serialized as `.pkl` files for fast inference at runtime.

## Project Structure

`app.py` contains the Streamlit application that loads the trained model and vectorizer, accepts user input, and returns a prediction. `model.pkl` is the serialized trained classifier. `vectorizer.pkl` is the fitted TF-IDF vectorizer used to transform input text. `requirements.txt` lists all Python dependencies required to run the project.

## Setup and Usage

Clone the repository and navigate into the project directory.

```bash
git clone https://github.com/AdityaRoy26/ML-Projects.git
cd ML-Projects/SMS-Spam-Classifier
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

Run the Streamlit application.

```bash
streamlit run app.py
```

Once the app is running, enter any SMS message into the input field and the model will classify it as spam or ham instantly.

## Tech Stack

Python, Scikit-learn, NLTK, Pandas, NumPy, Streamlit
