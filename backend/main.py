from flask import Flask, jsonify,blueprints
from flask_cors import CORS
import TextUtils

from controllers.UserController import user_controller
from controllers.RoomController import room_controller
from controllers.ReserveController import reserve_controller

api = Flask(__name__)

api.register_blueprint(user_controller, url_prefix='/api/users')
api.register_blueprint(room_controller, url_prefix='/api/rooms')
api.register_blueprint(reserve_controller, url_prefix='/api/reserves')

CORS(api)

@api.route('/')
def index():
    return jsonify({"message": "Welcome to the API!"})