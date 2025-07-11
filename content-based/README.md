# Book Recommendation System

A content-based book recommendation system with fuzzy title matching and cover image display, built with Python and Gradio.

## Features
- Content-based recommendations using TF-IDF and cosine similarity
- Fuzzy title matching with fallback to semantic similarity
- Book cover display with placeholder for missing images
- Clean Gradio web interface
- Handles large book datasets efficiently

## Project Structure
content-based_recommender/
├── data/
│   └── books_data.csv       # Your preprocessed dataset
├── utils/
│   ├── recommender.py       # Core recommendation functions
│   └── image_utils.py       # Cover image handling
├── app.py                   # Streamlit main app
├── requirements.txt         # Dependencies
└── README.md


## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/book-recommender.git
cd book-recommender

2. Install dependencies:
```bash
pip install -r requirements.txt
3. Run the app:
```bash
streamlit run app.py
```
