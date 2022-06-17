from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

from classes.Recommender import Recommender

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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