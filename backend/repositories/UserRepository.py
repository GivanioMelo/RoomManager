from repositories.BaseRepository import BaseRepository
from entities.User import User

class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__()
        self.tableName = 'users'
    
    def getByCredentials(self, login: str, password:str) -> User:
        query = f"SELECT * FROM users WHERE login = '{login}' AND password = '{password}'"
        result = self.executeQuery(query)
        if result:
            return User.from_dict(result[0])
        return None

    def getByJwtToken(self, jwt_token: str) -> User:
        query = f"SELECT * FROM users WHERE jwtToken = '{jwt_token}'"
        result = self.executeQuery(query)
        if result:
            return User.from_dict(result[0])
        return None
