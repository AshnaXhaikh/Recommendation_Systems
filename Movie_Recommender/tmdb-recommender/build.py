# app.py
import os
import openai
import pickle
import streamlit as st
from recommend import recommend, movies, fetch_poster
from utils.llm_helper import get_llm_response


st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("Movie Recommender System")
selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    recommendations, posters, selected_id = recommend(selected_movie)
    
    selected_poster = fetch_poster(selected_id)
    st.image(selected_poster, width=400)  

    # Display with columns
    st.markdown("### Recommended Movies:")
    cols = st.columns(5)
    for i in range(len(recommendations)):
        with cols[i]:
            st.image(posters[i], output_format='auto', width=250)
            st.caption(recommendations[i])
    
    # Get LLM insights
    prompt = f"""Give a short overview of the movie '{selected_movie}' including its genre, director, and cast (top 5 character names).
Also mention names of recommended movies along explainations how these recommended movies {recommendations} relate to the selected movie {selected_movie} — in terms of genre, direction, or cast similarities.
"""
    with st.spinner("Getting AI insights..."):
        try:
            insights = get_llm_response(prompt)
            st.markdown(f"{insights}")
        except Exception as e:
            st.error(f"LLM Error: {str(e)}")


# f"Explain why someone who likes '{selected_movie}' would enjoy these movies: {', '.join(recommendations)}"