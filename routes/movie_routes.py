from flask import request, jsonify, Blueprint
import requests
import json

from classes.Recommender import Recommender
from classes.Vector import Vector
from classes.Search import Search

movie_api = Blueprint('movie_api', __name__)

@movie_api.route('/movies/fetch/<id>', methods=['GET', 'POST'])
def fetch(id):

    data = requests.get(f"http://www.omdbapi.com/?i={id}&apikey=ac6564b1")

    return json.loads(data.text)

@movie_api.route('/movies/recommend/<id>', methods=['GET', 'POST'])
def recommend(id):
    args = request.args

    recommender = Recommender()
    print("================", args.get('page'))
    movies = recommender.get_recommendations(id)
    json_res = movies.to_dict(orient = 'records')
    return jsonify(json_res)

@movie_api.route('/movies/recommend/genres', methods=['POST'])
def vector():
    genres_list = str(request.form["genres"]).split(",")
    recommender = Vector(genres_list = genres_list)
    movies = recommender.get_recommendations()
    json_res = movies.to_dict(orient = 'records')
    return jsonify(json_res)

@movie_api.route('/movies/search', methods=['POST'])
def search():
    search_term = str(request.form["search_term"])
    recommender = Search(search_term = search_term)
    movies = recommender.get_recommendations()
    json_res = movies.to_dict(orient = 'records')
    return jsonify(json_res)