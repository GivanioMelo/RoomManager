from flask import Blueprint, jsonify, request
from workers.RoomWorker import RoomWorker
from entities.Room import Room

roomController = Blueprint('room_controller', __name__)
roomWorker = RoomWorker()

@roomController.route('/all', methods=['GET'])
def getAll():
    rooms = roomWorker.getAll()
    return jsonify([room.toDict() for room in rooms]), 200

@roomController.route('/<int:id>', methods=['GET'])
def getById(id:int):
    room = roomWorker.getById(id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    return jsonify(room.toDict()), 200

