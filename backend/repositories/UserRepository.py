from repositories.BaseRepository import BaseRepository
from entities.User import User
class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
    
    def create(self, user: User):
        command = f"""
        INSERT INTO users (name, email, login, password, jwtToken, isAdmin, isActive, creationUser, creationDate, updateUser, updateDate)
        VALUES ('{user.name}', '{user.email}', '{user.login}', '{user.password}', '{user.jwtToken}', {int(user.isAdmin)}, {int(user.isActive)}, {user.creationUser}, '{user.creationDate}', {user.updateUser}, '{user.updateDate}')
        """
        self.execute(command)
    
    def update(self, user: User):
        command = f"""
        UPDATE users
        SET name = '{user.name}', email = '{user.email}', login = '{user.login}', password = '{user.password}', jwtToken = '{user.jwtToken}', isAdmin = {int(user.isAdmin)}, isActive = {int(user.isActive)}, updateUser = {user.updateUser}, updateDate = '{user.updateDate}'
        WHERE id = {user.id}
        """
        self.execute(command)
    
    def delete(self, user_id: int):
        command = f"DELETE FROM users WHERE id = {user_id}"
        self.execute(command)

    def get_by_id(self, user_id: int) -> User:
        query = f"SELECT * FROM users WHERE id = {user_id}"
        result = self.executeQuery(query)
        if result:
            return User.from_dict(result[0])
        return None

    def get_all(self) -> list[User]:
        query = "SELECT * FROM users"
        results = self.executeQuery(query)
        return [User.from_dict(row) for row in results] if results else []
    
    def get_by_credentials(self, login: str, password:str) -> User:
        query = f"SELECT * FROM users WHERE login = '{login}' AND password = '{password}'"
        result = self.executeQuery(query)
        if result:
            return User.from_dict(result[0])
        return None

    def get_by_email(self, email: str) -> User:
        query = f"SELECT * FROM users WHERE email = '{email}'"
        result = self.executeQuery(query)
        if result:
            return User.from_dict(result[0])
        return None
    
    def get_by_jwt_token(self, jwt_token: str) -> User:
        query = f"SELECT * FROM users WHERE jwtToken = '{jwt_token}'"
        result = self.executeQuery(query)
        if result:
            return User.from_dict(result[0])
        return None
    
