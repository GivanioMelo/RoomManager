from flask import Blueprint, jsonify, request
from workers.ReserveWorker import ReserveWorker

reserve_controller = Blueprint('reserve_controller', __name__)
reserve_worker = ReserveWorker()

@reserve_controller.route('/getAll', methods=['GET'])
def getAllRserves():
    reserves = reserve_worker.get_all_reserves()
    return jsonify([reserve.to_dict() for reserve in reserves]), 200

@reserve_controller.route('byUser/<int:id>', methods=['GET'])
def get_reserves_by_user(id):
    reserves = reserve_worker.getReservesByUser(id)
    if not reserves: return jsonify({"error": "No reserves found for this user"}), 404
    return jsonify([reserve.toDict() for reserve in reserves]), 200

@reserve_controller.route('/create', methods=['POST'])
def create_reserve():
    data = request.json
    if not data or 'roomId' not in data or 'userId' not in data or 'startTime' not in data or 'endTime' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    reserve = reserve_worker.create_reserve(
        room_id=data['roomId'],
        user_id=data['userId'],
        start_time=data['startTime'],
        end_time=data['endTime']
    )
    
    if reserve: return jsonify(reserve.toDict()), 201
    else: return jsonify({"error": "Failed to create reserve"}), 500