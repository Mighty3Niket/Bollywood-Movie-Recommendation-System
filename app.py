import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    api_key = "a9287d76"
    url = f"http://www.omdbapi.com/?i={movie_id}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()  # Corrected: Add parentheses to call the method
    return data['Poster'] if 'Poster' in data and data['Poster'] != 'N/A' else None  # Handle cases where 'Poster' might not be in the response or is 'N/A'

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].imdbId
        poster = fetch_poster(movie_id)
        if poster:  # Only add the movie if it has a valid poster
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(poster)
            if len(recommended_movies) >= 5:  # Only keep the top 5 recommendations
                break
    
    return recommended_movies, recommended_movies_posters

st.title("Bollywood Movie Recommendation System")

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie = st.selectbox('Search', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    cols = st.columns(len(names))

    for i in range(len(names)):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i], use_column_width=True)  # Adjust image to fit the column width

st.caption("built by Triniket Maiti")