from flask import Flask, jsonify,blueprints
from flask_cors import CORS
import TextUtils

from controllers.UserController import userController
from controllers.RoomController import roomController
from controllers.ReserveController import reserveController

api = Flask(__name__)

api.register_blueprint(userController, url_prefix='/api/users')
api.register_blueprint(roomController, url_prefix='/api/rooms')
api.register_blueprint(reserveController, url_prefix='/api/reserves')

CORS(api)

@api.route('/')
def index():
    return jsonify({"message": "Welcome to the API!"})