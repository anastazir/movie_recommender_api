from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/about', methods=['GET'])
def about():
    return {'datasets_used': ["https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset",
                            "https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata"],
            'type': 'Movie Recommender API',
            'description': 'This is a movie recommender API system that uses the movie data from the Kaggle dataset.',
            }

@app.route('/fetch/<id>', methods=['GET', 'POST'])
def fetch(id):

    data = requests.get(f"http://www.omdbapi.com/?i={id}&apikey=ac6564b1")

    return json.loads(data.text)