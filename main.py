from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/about', methods=['GET'])
def about():
    return {'datasets_used': ["https://www.kaggle.com/code/logicalbin123/movie-recommender/data",
                            "https://www.kaggle.com/code/logicalbin123/movie-recommender/data"],
            'type': 'Movie Recommender API',
            'description': 'This is a movie recommender API system that uses the movie data from the Kaggle dataset.',
            }

