from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
import warnings

from classes.Recommender import Recommender
from classes.Vector import Vector
from classes.Search import Search

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

warnings.filterwarnings("ignore")

@app.route('/fetch/<id>', methods=['GET', 'POST'])
def fetch(id):

    data = requests.get(f"http://www.omdbapi.com/?i={id}&apikey=ac6564b1")

    return json.loads(data.text)

@app.route('/recommend/<name_or_id>', methods=['GET', 'POST'])
def recommend(name_or_id):
    if str(name_or_id).startswith('tt') and len(str(name_or_id)) == 9:
        type = "id"
    else:
        type = "title"
    recommender = Recommender(type = type)

    movies = recommender.get_recommendations(a = name_or_id)
    json_res = movies.to_dict(orient = 'records')
    return jsonify(json_res)

@app.route('/recommend/genres', methods=['POST'])
def vector():
    genres_list = str(request.form["genres"]).split(",")
    recommender = Vector(genres_list = genres_list)
    movies = recommender.get_recommendations()
    json_res = movies.to_dict(orient = 'records')
    return jsonify(json_res)

@app.route('/search', methods=['POST'])
def search():
    search_term = str(request.form["search_term"])
    recommender = Search(search_term = search_term)
    movies = recommender.get_recommendations()
    json_res = movies.to_dict(orient = 'records')
    return jsonify(json_res)