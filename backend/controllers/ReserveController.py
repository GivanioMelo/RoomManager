from flask import Blueprint, jsonify, request
from workers.ReserveWorker import ReserveWorker

reserveController = Blueprint('reserveController', __name__)
reserveWorker = ReserveWorker()

@reserveController.route('/getAll', methods=['GET'])
def getAllRserves():
    reserves = reserveWorker.getAll()
    return jsonify([reserve.to_dict() for reserve in reserves]), 200

@reserveController.route('byUser/<int:id>', methods=['GET'])
def getReservesByUser(id):
    reserves = reserveWorker.getReservesByUser(id)
    if not reserves: return jsonify({"error": "No reserves found for this user"}), 404
    return jsonify([reserve.toDict() for reserve in reserves]), 200

@reserveController.route('/create', methods=['POST'])
def createReserve():
    data = request.json
    if not data or 'roomId' not in data or 'userId' not in data or 'startTime' not in data or 'endTime' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    reserve = reserveWorker.create(
        room_id=data['roomId'],
        user_id=data['userId'],
        start_time=data['startTime'],
        end_time=data['endTime']
    )
    
    if reserve: return jsonify(reserve.toDict()), 201
    else: return jsonify({"error": "Failed to create reserve"}), 500