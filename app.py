import streamlit as st
import pandas as pd
from PIL import Image
import requests
import io
from PIL import Image, ImageDraw, ImageFont
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("books_data.csv")
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = tfidf.fit_transform(df['text_for_tfidf'])
    return df, tfidf, tfidf_matrix

df, tfidf, tfidf_matrix = load_data()

# Image loader with placeholder
def get_cover(url):
    try:
        response = requests.get(url, timeout=5)
        return Image.open(io.BytesIO(response.content))
    except:
        img = Image.new('RGB', (200, 300), '#222222')
        draw = ImageDraw.Draw(img)
        draw.text((40, 140), "No Cover", fill="white")
        return img

# Recommendation function
def recommend(title):
    title = str(title).lower().strip()
    matches = df[df['title'].str.contains(title, case=False)]
    if not matches.empty:
        cosine_sim = cosine_similarity(tfidf.transform(matches['text_for_tfidf']), tfidf_matrix)
        return matches.iloc[cosine_sim.mean(axis=1).argsort()[::-1]]
    return df.sample(5)  # Fallback

# Streamlit UI
st.title("📚 Book Recommender")
search = st.text_input("Title/Author/Genre", placeholder="Harry Potter")

if st.button("Recommend"):
    results = recommend(search)
    cols = st.columns(5)
    for idx, row in results.head(5).iterrows():
        with cols[idx % 5]:
            st.image(get_cover(row['img_url']), width=150)
            st.caption(f"**{row['title']}**")
            st.text(f"by {row['author']}")


