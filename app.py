from flask import Flask, render_template, request
import pickle
import requests

import os
import gdown

FILE_ID = "1-k1vzgLLcA5vmryX-OvHPAj1eootIjhc"
OUTPUT = "similiarity.pkl"

if not os.path.exists(OUTPUT):
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    gdown.download(url, OUTPUT, quiet=False, fuzzy=True)

app = Flask(__name__)

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similiarity.pkl", "rb"))

API_KEY = os.getenv("82482b695f7c868afac954cb7ed65715")



def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        data = requests.get(url).json()

        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

    except:
        pass

    return "https://via.placeholder.com/500x750?text=No+Poster"


def recommend(movie):

    index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    names = []
    posters = []

    for i in distances[1:6]:

        movie_id = movies.iloc[i[0]].movie_id

        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters


@app.route("/", methods=["GET", "POST"])
def home():

    movie_list = movies["title"].tolist()

    recommended_movies = []
    recommended_posters = []

    selected_movie = None

    if request.method == "POST":

        selected_movie = request.form["movie"]

        recommended_movies, recommended_posters = recommend(selected_movie)

    return render_template(
        "index.html",
        movie_list=movie_list,
        selected_movie=selected_movie,
        recommended_movies=recommended_movies,
        recommended_posters=recommended_posters
    )


if __name__ == "__main__":
    app.run(debug=True)