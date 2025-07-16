from flask import Blueprint, jsonify, request
from workers.UserWorker import UserWorker
from entities.User import User

user_controller = Blueprint('user_controller', __name__)
user_worker = UserWorker()

def validate_user_data(data):
    required_fields = ['name', 'email', 'login', 'password']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing or empty field: {field}"
    if 'email' in data and '@' not in data['email']:
        return False, "Invalid email format"
    if 'password' in data and len(data['password']) < 6:
        return False, "Password must be at least 6 characters long"
    if 'isAdmin' in data and not isinstance(data['isAdmin'], bool):
        return False, "isAdmin must be a boolean value"
    return True, ""

@user_controller.route('/create', methods=['POST'])
def create_user():
    data = request.json
    is_valid, error_message = validate_user_data(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400
    
    if user_worker.user_repository.get_by_email(data.get('email')):
        return jsonify({"error": "Email already exists"}), 400
    
    if user_worker.user_repository.get_by_login(data.get('login')):
        return jsonify({"error": "Login already exists"}), 400
    
    if not User.fromDict(data).is_valid():
        return jsonify({"error": "Invalid user data"}), 400
    
    # Create user
    user_id = user_worker.create_user(
        name=data.get('name'),
        email=data.get('email'),
        login=data.get('login'),
        password=data.get('password'),
        is_admin=data.get('isAdmin', False)
    )
    return jsonify({"user_id": user_id}), 201

@user_controller.route('/login', methods=['POST'])
def login_user(login, password):
    user = user_worker.user_repository.get_by_login(login, password)
    if not user:
        return None
    return user