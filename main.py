from flask import Flask, request, jsonify
from flask_cors import CORS
import warnings
from routes.movie_routes import movie_api


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

warnings.filterwarnings("ignore")

app.register_blueprint(movie_api)



