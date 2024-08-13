import streamlit as st
import pickle
import pandas as pd

st.title('Movie Recommendation System')
movies=pickle.load(open('movie.pkl','rb')) # load the model
similarity=pickle.load(open('similarity.pkl','rb'))

movie=movies['title'].values # movie titles

# selecting Movie Name
option = st.selectbox(
    'Select Movie Name-->',
    movie)

# recommend function to get the movie name
def recommend(movie):
    ind=movies[movies['title']==movie].index[0]
    distances=similarity[ind]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    recommended_movies=[]
    recommended_posters=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching posters
        recommended_posters.append(movies.iloc[i[0]].poster)
    return recommended_movies,recommended_posters


if st.button('Recommend'):
    st.write('Recommended Movies are-->')
    movie_name, movie_poster = recommend(option)
    n = len(movie_name)
    rows = n // 5 + min(n % 5, 1) # calculate number of rows needed
    for i in range(rows):
        row = st.columns(5)
        for j in range(min(n - i * 5, 5)):
            with row[j]:
                st.text(movie_name[i * 5 + j])
                st.image(movie_poster[i * 5 + j])