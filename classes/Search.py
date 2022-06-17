import pandas as pd
import re
import math
from collections import Counter



class Search():
    def __init__(self, search_term):
        self.search_term = search_term
        self.df = pd.read_csv("datasets\merged\merged.csv")
        self.names_df = self.df[["name", "imdb_id"]]

    def get_cosine(self, vec2):

        intersection = set(self.vec1.keys()) & set(vec2.keys())
        numerator = sum([self.vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([self.vec1[x]**2 for x in self.vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    def text_to_vector(self, text):
        word = re.compile(r'\w+')
        words = word.findall(text)
        return Counter(words)


    def get_result(self, text2):
        self.vec1 = self.text_to_vector(self.search_term)
        vector2 = self.text_to_vector(text2)
        cosine_result = self.get_cosine(vector2)
        return cosine_result

    def get_results(self):

        self.search_term = self.search_term.lower()
        self.names_df["scores"] = self.names_df["name"].apply(lambda x: self.get_result(x.lower()))
        results = self.names_df.sort_values(by = "scores", ascending = False).head(30)
        results.drop(columns = ["scores"], inplace = True)
        return results

    def get_recommendations(self):
        results = self.get_results()
        rm = results[["imdb_id"]].merge(self.df, on="imdb_id")
        rm = rm[["id","imdb_id","name", "year","poster","runtime","adult","rating", 'popularity']]
        del self.df, self.names_df
        return rm
