# Movie Recommender System
A content-based movie recommendation system that suggests similar movies based on your selection. Built with Python and deployed on Hugging Face Spaces.

**Live Demo:** [Try it on Hugging Face Spaces](https://huggingface.co/spaces/AdityaRoy26/movie-recommender)

## Overview
Given a movie title, the system analyzes metadata such as genres, keywords, cast, crew, and overview to return the top 5 most similar movies using cosine similarity.

## Tech Stack
- **Language:** Python
- **ML / NLP:** Scikit-learn, NLTK
- **Data Processing:** Pandas, NumPy
- **Web App:** Streamlit
- **Deployment:** Hugging Face Spaces

## How It Works
1. Movie metadata (genres, cast, crew, keywords, overview) is cleaned and merged into a single tags feature per movie.
2. Tags are vectorized using `CountVectorizer`.
3. Cosine similarity is computed between all movie vectors.
4. On user input, the top 5 most similar movies are returned.

## Project Structure

```
ML-Projects/
├── app.py               # Streamlit web application
├── movies.pkl           # Preprocessed movie data
├── similarity.pkl       # Precomputed cosine similarity matrix
├── requirements.txt     # Python dependencies
├── .gitattributes
└── .gitignore
```
## Run Locally
```bash
git clone https://github.com/AdityaRoy26/ML-Projects.git
cd ML-Projects
pip install -r requirements.txt
streamlit run app.py
```
## Dataset

Trained on the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle, containing metadata for approximately 5,000 movies.
## Author
Aditya Roy — [GitHub](https://github.com/AdityaRoy26) | [Hugging Face](https://huggingface.co/AdityaRoy26)
