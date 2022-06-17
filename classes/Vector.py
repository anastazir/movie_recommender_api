import pandas as pd
import math
import ast
from config import *

class Vector():
    def __init__(self, genres_list):
        self.genres_list = genres_list
        self.vector = self.create_vector()

    def create_vector(self):
        v = []
        for g in GENERS:
            if g in self.genres_list:
                v.append(1)
            else:
                v.append(0)
        return v

    def cosine_similarity(self, vec):
        "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
        vec = ast.literal_eval(vec)
        if sum(vec) == 0: return 0
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(self.vector)):
            x = self.vector[i]; y = vec[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        return sumxy/math.sqrt(sumxx*sumyy)

    def get_recommendations(self):
        vd = pd.read_csv("datasets/vector/vector.csv")
        vd = vd[["id_x","name","imdb_id","vectors"]]
        vd["scores"] = vd["vectors"].apply(self.cosine_similarity)
        results = vd.sort_values(by = "scores", ascending = False).head(50)
        results.drop(columns = ["scores"], inplace = True)
        del vd
        return results
