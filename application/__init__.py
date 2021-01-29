from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from flask_compress import Compress


app = Flask(__name__)
Compress(app)
CORS(app)
api = Api(app)

from application.routes import image_return