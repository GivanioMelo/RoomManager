from flask import Blueprint, jsonify, request
from workers.RoomWorker import RoomWorker
from entities.Room import Room

room_controller = Blueprint('room_controller', __name__)
room_worker = RoomWorker()

@room_controller.route('/all', methods=['GET'])
def get_all_rooms():
    rooms = room_worker.get_all_rooms()
    return jsonify([room.toDict() for room in rooms]), 200

@room_controller.route('/<int:room_id>', methods=['GET'])
def get_room(room_id):
    room = room_worker.get_room_by_id(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    return jsonify(room.toDict()), 200

