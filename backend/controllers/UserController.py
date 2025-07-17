from flask import Blueprint, jsonify, request
from workers.UserWorker import UserWorker
from entities.User import User

userController = Blueprint('user_controller', __name__)
userWorker = UserWorker()

#TODO mover isso aqui pro worker, onde é o lugar de lógica
def validateUser(data):
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

@userController.route('/create', methods=['POST'])
def createUser():
    data = request.json
    is_valid, error_message = validateUser(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    #TODO refazer respeitando as camadas    
    # if userWorker.user_repository.get_by_email(data.get('email')):
    #     return jsonify({"error": "Email already exists"}), 400
    
    # if userWorker.user_repository.get_by_login(data.get('login')):
    #     return jsonify({"error": "Login already exists"}), 400
    
    if not User.fromDict(data).is_valid():
        return jsonify({"error": "Invalid user data"}), 400
    
    # Create user
    userId = userWorker.create(
        name=data.get('name'),
        email=data.get('email'),
        login=data.get('login'),
        password=data.get('password'),
        is_admin=data.get('isAdmin', False)
    )
    return jsonify({"userId": userId}), 201

@userController.route('/login', methods=['POST'])
def loginUser():
    data = request.json
    login = data.get("login")
    password = data.get("password")
    user = userWorker.login(login,password)
    if not user:
        return None, 401
    return jsonify({"userId": user.id, "token":user.token}), 200