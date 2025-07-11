import streamlit as st
from sentence_transformers import SentenceTransformer
import pandas as pd
import faiss


# Load pre-built index and metadata
@st.cache_resource
def load_resources():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    index = faiss.read_index(r'D:\GenAI\BookRecommender\data\index.faiss')
    df = pd.read_parquet(r'D:\GenAI\BookRecommender\data\books_metadata.parquet')
    return model, index, df

model, index, df = load_resources()

#--- Streamlit UI ----
st.title("📚 Book Recommender")
st.markdown('Discover books tailored to your interests!')

# Search input 
query = st.text_input('What kind of books are you looking for?',
                      placeholder='e.g. science , history, self guidance...')
if query:
    # Get recommendations
    query_embedding = model.encode([query]).astype('float32')
    distances, indices = index.search(query_embedding, 5)
    recommended = df.iloc[indices[0]]

    # Display results
    st.subheader("Recommended Books:")
    for i, book in recommended.iterrows():
        with st.container(border=True):
            col1, col2 = st.columns([1, 3])

            # Book cover
            with col1:
                if pd.notna(book['thumbnail']):
                    st.image(book['thumbnail'], width=150)
                else:
                    st.image('https://via.placeholder.com/150', width=150)
            
            # Book details
            with col2:
                st.markdown(f"### [{book['title']}](https://www.google.com/search?q={book['title'].replace(' ', '+')}+book)")

                # Authors and categories
                if pd.notna(book['authors']):
                    st.markdown(f"**By:** {book['authors']}")
                if pd.notna(book['categories']):
                    st.markdown(f"**Genre:** {book['categories']}")

                # Rating and Publication info 
                cols = st.columns(3)
                with cols[0]:
                    st.metric('Rating', f"{book['average_rating']:.1f}/5" if pd.notna(book['average_rating']) else "N/A")
                with cols[1]:
                    st.metric('Pages', book['num_pages'] if pd.notna(book['num_pages']) else "N/A")
                with cols[2]:
                    st.metric('Year', int(book['published_year']) if pd.notna(book['published_year']) else 'N/A')

                # Description
                if pd.notna(book['description']):
                    with st.expander('Description'):
                        st.write(book['description'])

                # Additional actions
                st.button("Save to favorites", key=f"fav_{i}")
                st.link_button("Find this book", f"https://www.google.com/search?q={book['title'].replace(' ', '+')}+{book['authors'].replace(' ', '+')}")

                # Show raw data for debugging (optional)
    with st.expander("Debug: Show raw data"):
        st.write(recommended)


