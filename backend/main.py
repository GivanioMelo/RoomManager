from flask import Flask, jsonify,blueprints
from flask_cors import CORS
import TextUtils

from controllers.UserController import user_controller

api = Flask(__name__)

api.register_blueprint(user_controller, url_prefix='/api/users')

CORS(api)

@api.route('/')
def index():
    return jsonify({"message": "Welcome to the API!"})