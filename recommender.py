import pandas as pd
import pickle

df = pd.read_csv("./data/results.csv")

with open("./data/cosine_sim2.pkl", "rb") as f:
    model = pickle.load(f)


def get_recommendations(id, n=10):
    # Get the index of the movie that matches the id
    idx = df[df["imdb_id"] == id].index[0]

    # Get the similarity scores between the movie and all other movies
    sim_scores = list(enumerate(model[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:n + 1]

    # Get the movie ids from the similatiry scores
    movie_ids = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return df.iloc[movie_ids][["tittle", "genres"]]
