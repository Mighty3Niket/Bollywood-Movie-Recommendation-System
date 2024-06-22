import numpy as np
import pandas as pd
import ast
import sklearn
import nltk
import pickle

movies = pd.read_csv('BollywoodMovieDetail.csv')
movies = movies[['imdbId', 'title', 'genre', 'actors', 'directors']]
movies = movies.dropna()
movies = movies.reset_index()

def convert(obj):
  L=list(obj.split(" | "))
  return L

movies['genre'] = movies['genre'].apply(convert)
movies['actors'] = movies['actors'].apply(convert)
movies['directors'] = movies['directors'].apply(convert)

movies['genre'] = movies['genre'].apply(lambda x:[i.replace(" ","") for i in x])
movies['actors'] = movies['actors'].apply(lambda x:[i.replace(" ","") for i in x])
movies['directors'] = movies['directors'].apply(lambda x:[i.replace(" ","") for i in x])

movies['tags'] = movies['genre'] + movies['actors'] + movies['directors']

new_df = movies[['imdbId', 'title', 'tags']]
new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x))
new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()
cv.get_feature_names_out()

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
  y = []
  for i in text.split():
    y.append(ps.stem(i))
  return " ".join(y)

new_df['tags'] = new_df['tags'].apply(stem)

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)

def recommend(movie):
  movie_index = new_df[new_df['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
  for i in movies_list:
    print(new_df.iloc[i[0]].title)

#print(movies['title'].index)

pickle.dump(new_df.to_dict(), open('movie_dict.pkl','wb'))
pickle.dump(similarity, open('similarity.pkl','wb'))