from repositories.BaseRepository import BaseRepository
from entities.User import User

class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__()
        self.tableName = 'users'
    
    def create(self,user:User):
        query = f"""
            INSERT INTO {self.tableName} (login, password, name, email)
            VALUES ('{user.login}', '{user.password}', '{user.name}', '{user.email}')
        """
        if user.creationUserId and user.updateUserId:
            query = f"""
                INSERT INTO {self.tableName} (login, password, name, email, creationUser, updateUser)
                VALUES ('{user.login}', '{user.password}', '{user.name}', '{user.email}',{user.creationUserId}, {user.updateUserId})
            """
        self.executeNonQuery(query)

    def getById(self, id:int):
        query = f"SELECT * FROM {self.tableName} WHERE id = '{id}'"
        result = self.executeQuery(query)
        if result:
            return User.fromDict(result[0])
        return None


    def getByCredentials(self, login: str, password:str) -> User:
        query = f"SELECT * FROM {self.tableName} WHERE login = '{login}' AND password = '{password}'"
        result = self.executeQuery(query)
        if result:
            return User.fromDict(result[0])
        return None

    def getByToken(self, jwt_token: str) -> User:
        query = f"SELECT * FROM users WHERE jwtToken = '{jwt_token}'"
        result = self.executeQuery(query)
        if result:
            return User.fromDict(result[0])
        return None
