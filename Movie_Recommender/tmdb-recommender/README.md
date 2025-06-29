# 🎬 TMDB Movie Recommender System with LLM Insights

Welcome to my Movie Recommender System built using **Python**, **Langchain**, **Streamlit**, and **LLMs**! This project allows users to select a movie and get similar movie recommendations based on **content-based filtering**. The system also fetches **movie posters** and provides **AI-generated insights** using an integrated **Large Language Model (LLM)**.

---

## 📌 Features

✅ Content-based movie recommendation using similarity scores  
✅ Poster fetching via TMDB API  
✅ LLM (e.g., Gemini) integration for AI-powered movie overviews and reasoning  
✅ Streamlit web interface  
✅ Modern, interactive UI with main movie poster + related movies  

---

## 🧠 How It Works

1. **Similarity Engine**: Precomputed cosine similarity matrix (from `movies.pkl` and `similarity.pkl`)
2. **Poster Fetching**: Uses TMDB API to fetch posters based on `movie_id`
3. **LLM Insights**: Generates short summaries and explains why the recommendations make sense
4. **Streamlit UI**: Simple dropdown and button-based interface for interaction

---

## 🔧 Setup Instructions

1. **Clone the Repo**
   ```bash
   git clone https://github.com/yourusername/tmdb-recommender.git
   cd tmdb-recommender
