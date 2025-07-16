from entities.Entity import Entity

class User(Entity):
    name:str
    email:str
    login:str
    password:str
    token:str
    isAdmin:bool
    isActive:bool

    def __init__(self, id: int = 0, 
                name: str = "", 
                email: str = "", 
                login: str = "", 
                password: str = "", 
                token: str = "", 
                isAdmin: bool = False, 
                isActive: bool = True):
        super().__init__(id=id)
        self.name = name
        self.email = email
        self.login = login
        self.password = password
        self.token = token
        self.isAdmin = isAdmin
        self.isActive = isActive

        self.reserves = []  # Placeholder for reserves, to be populated later
        self.issues = []  # Placeholder for issues, to be populated later
    
    def __str__(self):
        return f"""
            User\n
                \t id={self.id},\n
                \t name={self.name},\n
                \t email={self.email},\n
                \t login={self.login},\n
                \t isAdmin={self.isAdmin},\n
                \t isActive={self.isActive}\n
        """
    
    def __repr__(self): return self.__str__()
    
    def toDict(self):
        data = super().toDict()
        data.update({
            "name": self.name,
            "email": self.email,
            "isAdmin": self.isAdmin,
            "isActive": self.isActive
        })
        if self.reserves: data["reserves"] = [reserve.to_dict() for reserve in self.reserves]
        if self.issues: data["issues"] = [issue.to_dict() for issue in self.issues]
        return data

    @staticmethod
    def fromDict(data):
        user = User()
        user.id = data.get("id", 0)
        user.name = data.get("name", "")
        user.email = data.get("email", "")
        user.login = data.get("login", "")
        user.password = data.get("password", "")
        user.token = data.get("token", "")
        user.isAdmin = data.get("isAdmin", False)
        user.isActive = data.get("isActive", True)
        user.creationUserId = data.get("creationUser", 0)
        user.creationDate = data.get("creationDate", "")
        user.updateUserId = data.get("updateUser", 0)
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
        return json.dumps(self.toDict())
    
    @staticmethod
    def from_json(json_str):
        import json
        data = json.loads(json_str)
        return User.fromDict(data)