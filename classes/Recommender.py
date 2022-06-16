import pandas as pd
import pickle
import gzip

class Recommender():
    def __init__(self, NAME = "KCWG"):
        self.NAME = NAME
        self.df = pd.read_csv("datasets\preprocessed\preprocessed_id.csv")
        self.model = self.load_model()

    def load_model(self):
        fp = gzip.open(f'models/{self.NAME}.data','rb')
        cosine_sim = pickle.load(fp)
        fp.close()
        return cosine_sim

    # Function that takes in movie title as input and outputs most similar movies
    def get_recommendations_title(self, title):
        # Get the index of the movie that matches the title
        try:
            idx = self.df.index[self.df['name'] == title].tolist()[0]
        except:
            print("Movie not found in our database")
            return
        # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(self.model[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 50 most similar movies
        sim_scores = sim_scores[1:51]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 50 most similar movies
        return self.df.iloc[movie_indices]

    # Function that takes in imdb id as input and outputs most similar movies
    def get_recommendations_id(self, imbdId):
        # Get the index of the movie that matches the title
        idx = self.df.index[self.df['imdb_id'] == imbdId].tolist()[0]

        # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(self.model[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 50 most similar movies
        sim_scores = sim_scores[1:51]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 50 most similar movies
        return self.df[['name', "imdb_id"]].iloc[movie_indices]