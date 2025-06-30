from flask import Flask, render_template, request
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

# load the dataset
df = pd.read_csv("clustered_df.csv")

# numerical features list
numerical_features = [
    "valence",
    "year",
    "acousticness",
    "danceability",
    "duration_ms",
    "energy",
    "explicit",
    "instrumentalness",
    "key",
    "liveness",
    "loudness",
    "mode",
    "popularity",
    "speechiness",
    "tempo",
]


# recommend songs function
def recommend_songs(song_name, df, num_recommendations=7):
    # get the cluster of the input song
    song_cluster = df[df["name"] == song_name]["Cluster"].values[0]

    # filter songs from the same cluster
    same_cluster_songs = df[df["Cluster"] == song_cluster]

    # calculate similarity within the same cluster
    song_index = same_cluster_songs[same_cluster_songs["name"] == song_name].index[0]
    cluster_features = same_cluster_songs[numerical_features]
    similarity = cosine_similarity(cluster_features, cluster_features)

    # get top recommendations
    similar_songs = np.argsort(similarity[song_index])[-(num_recommendations + 1) : -1][
        ::-1
    ]
    recommendations = same_cluster_songs.iloc[similar_songs][
        ["name", "year", "artists"]
    ]

    return recommendations


# app
app = Flask(__name__)


# Routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/songs-list")
def songs_list():
    return render_template("songs.html")


@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    recommendations = []
    if request.method == "POST":
        song_name = request.form.get("song_name")

        try:
            recommendations = recommend_songs(song_name, df).to_dict(orient="records")
        except Exception as e:
            recommendations = [{"name": "error", "year": "2001", "artist": "invalid"}]

        return render_template("index.html", recommendations=recommendations)


# driver code
if __name__ == "__main__":
    app.run(debug=True)
