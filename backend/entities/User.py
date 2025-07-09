from entities.Entity import Entity

class User(Entity):
    name:str
    email:str
    login:str
    password:str
    token:str
    isAdmin:bool
    isActive:bool

    def __init__(self):
        super().__init__()
        self.name = ""
        self.email = ""
        self.login = ""
        self.password = ""
        self.token = ""
        self.isAdmin = False
        self.isActive = True
    
    def __str__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email}, login={self.login}, password={self.password}, jwtToken={self.token}, isAdmin={self.isAdmin}, isActive={self.isActive})"
    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "name": self.name,
            "email": self.email,
            "login": self.login,
            "password": self.password,
            "token": self.token,
            "isAdmin": self.isAdmin,
            "isActive": self.isActive
        })
        return data
    
    @staticmethod
    def from_dict(data):
        user = User()
        user.id = data.get("id", 0)

        user.name = data.get("name", "")
        user.email = data.get("email", "")
        user.login = data.get("login", "")
        user.password = data.get("password", "")
        user.token = data.get("token", "")
        user.isAdmin = data.get("isAdmin", False)
        user.isActive = data.get("isActive", True)

        user.creationUser = data.get("creationUser", 0)
        user.creationDate = data.get("creationDate", "")
        user.updateUser = data.get("updateUser", 0)
        user.updateDate = data.get("updateDate", "")

        return user
    
    def is_valid(self):
        if not self.name or not self.email or not self.login or not self.password:
            return False
        if "@" not in self.email:
            return False
        if len(self.password) < 6:
            return False
        return True

    def to_json(self):
        import json
        return json.dumps(self.to_dict())
    
    @staticmethod
    def from_json(json_str):
        import json
        data = json.loads(json_str)
        return User.from_dict(data)