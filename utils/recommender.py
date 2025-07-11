import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

from utils.image_utils import get_cover_image, is_placeholder

# Initialize globally
df = pd.read_csv("data/books_data.csv")
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['text_for_tfidf'])

def recommend_books(book_title):
    """Your existing Colab function"""
    original_input = book_title
    book_title = str(book_title).lower().strip()
    df['title_clean'] = df['title'].str.lower().str.strip()
    
    # Initialize message
    status_message = ""
    
    # Step 1: Exact match
    exact_matches = df[df['title_clean'] == book_title]
    
    if not exact_matches.empty:
        status_message = f"Found exact matches for: '{original_input}'"
        results = exact_matches
    else:
        # Step 2: Partial match with word boundaries
        import re
        pattern = fr'\b{re.escape(book_title)}\b'
        title_matches = df[df['title_clean'].str.contains(pattern, case=False, na=False, regex=True)]
        
        if not title_matches.empty:
            status_message = f"Found partial matches for: '{original_input}'"
            # Rank by TF-IDF similarity
            tfidf_matches = tfidf.transform(title_matches['text_for_tfidf'])
            cosine_sim = cosine_similarity(tfidf_matches, tfidf_matrix)
            top_indices = cosine_sim.mean(axis=1).argsort()[-5:][::-1]
            results = title_matches.iloc[top_indices]
        else:
            status_message = f"No title matches for: '{original_input}'. Showing similar books."
            # Step 3: Semantic similarity fallback
            query_vec = tfidf.transform([book_title])
            cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
            top_indices = cosine_sim.argsort()[-5:][::-1]
            results = df.iloc[top_indices]
    
    # Prepare output with cover status tracking
    output = []
    covers_found = 0
    
    for _, row in results.iterrows():
        cover = get_cover_image(row['img_url'])
        if is_placeholder(cover):
            output.append((cover, f"{row['title']}\nby {row['author']}\n(No cover found)"))
        else:
            output.append((cover, f"{row['title']}\nby {row['author']}"))
            covers_found += 1
    
    # Update status message with cover info
    if covers_found < len(results):
        status_message += f" ({len(results)-covers_found} covers missing)"
    
    return output, status_message
    
    return output, status_message