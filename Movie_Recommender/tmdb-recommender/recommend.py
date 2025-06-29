import pickle

# Load pickled data
movies = pickle.load(open('data/movies.pkl', 'rb'))
similarity = pickle.load(open('data/similarity.pkl', 'rb'))

# def recommend(movie_title):
#     try:
#         matched = movies[movies['title'] == movie_title]
#         if matched.empty:
#             return ["Movie not found."]
        
#         index = matched.index[0]
#         distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)
#         recommendations = []
#         for i in distances[1:6]:
#             recommendations.append(movies.iloc[i[0]].title)
#         return recommendations
#     except Exception as e:
#         return [f"Error occurred: {str(e)}"]

    

import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=e2a6e1698f8934f2de85aedf29e3e2b4&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    return "https://image.tmdb.org/t/p/w500/" + poster_path
    

def recommend(movie_title):
    
    index = movies[movies['title'] == movie_title].index[0]
    selected_movie_id = movies.iloc[index].movie_id

    distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)

    recommended_movies = []
    recommended_posters = []

    for i in distances[1:6]:
        movie_idx = i[0]
        movie_data = movies.iloc[movie_idx]
        recommended_movies.append(movie_data.title)
        recommended_posters.append(fetch_poster(movie_data.movie_id))

    # Debug print to check the return values
    print("Recommended Movies:", recommended_movies)
    print("Recommended Posters:", recommended_posters)

    return recommended_movies, recommended_posters, selected_movie_id









