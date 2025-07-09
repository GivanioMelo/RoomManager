from entities.User import User
from repositories.UserRepository import UserRepository
from datetime import datetime
from flask import session

import jwt
import hashlib
import bcrypt

class UserWorker:
    userRepository: UserRepository

    def __init__(self):
        self.userRepository = UserRepository()
    
    def create_user(self, name: str, email: str, login: str, password: str, is_admin: bool = False) -> int:
        user = User()
        user.name = name
        user.email = email
        user.login = login
        user.password = password
        user.token = ""
        user.isAdmin = is_admin
        user.isActive = True
        user.creationUser = 1  # Assuming a default user ID for creation
        user.creationDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user.updateUser = 1
        user.updateDate = user.creationDate
        self.userRepository.create(user)
        return user.id
    
    def update_user(self, user_id: int, name: str, email: str, login: str, password: str, is_admin: bool = False) -> bool:
        user = self.userRepository.get_by_id(user_id)
        if not user:
            return False
        user.name = name
        user.email = email
        user.login = login
        user.password = hashlib.sha256(password.encode()).hexdigest()  # Hashing the password
        user.jwtToken = ""
        user.isAdmin = is_admin
        user.isActive = True
        user.updateUser = session.get('user_id', 1)  # Assuming the current user ID is stored in session
        user.updateDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.userRepository.update(user)
        return True
    
    def delete_user(self, user_id: int) -> bool:
        user = self.userRepository.get_by_id(user_id)
        if not user:
            return False
        self.userRepository.delete(user_id)
        return True

    def get_user_by_id(self, user_id: int) -> User:
        user = self.userRepository.get_by_id(user_id)
        if not user:
            return None
        return user

    def login(self, login: str, password: str) -> User:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Check if the user exists with the provided login and hashed password
        user = self.userRepository.getByCredentials(login, hashed_password)
        if not user:
            return None
        
        token = jwt.encode(
            {"user_id": user.id, "exp": datetime.utcnow().timestamp() + 3600},  # Token valid for 1 hour
            "your_secret_key",  # Replace with your actual secret key
            algorithm="HS256"
        )
        encryptedToken = bcrypt.hashpw(token.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user.token = encryptedToken
        
        user.updateUser = session.get('user_id', 1)
        user.updateDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.userRepository.update(user)
        session['user_id'] = user.id
        session['jwt_token'] = user.token
        return user
    
    def logout(self) -> bool:
        if 'user_id' in session:
            user_id = session['user_id']
            user = self.userRepository.get_by_id(user_id)
            if user:
                user.jwtToken = ""
                user.updateUser = session.get('user_id', 1)
                user.updateDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.userRepository.update(user)
            session.pop('user_id', None)
            session.pop('jwt_token', None)
            return True
        return False
    
    def get_all_users(self) -> list[User]:
        users = self.userRepository.get_all()
        return users
    
    def get_user_by_email(self, email: str) -> User:
        user = self.userRepository.get_by_email(email)
        if not user:
            return None
        return user
    
    def get_user_by_jwt_token(self, jwt_token: str) -> User:
        user = self.userRepository.getByJwtToken(jwt_token)
        if not user:
            return None
        return user