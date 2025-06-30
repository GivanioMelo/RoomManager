class Entity:
    id: int
    creationUser: int
    creationDate: str
    updateUser: int
    updateDate: str

    def __init__(self):
        self.id = 0
        self.creationUser = 0
        self.creationDate = ""
        self.updateUser = 0
        self.updateDate = ""
    
    def __str__(self):
        return f"Entity(id={self.id}, creationUser={self.creationUser}, creationDate={self.creationDate}, updateUser={self.updateUser}, updateDate={self.updateDate})"
    
    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            "id": self.id,
            "creationUser": self.creationUser,
            "creationDate": self.creationDate,
            "updateUser": self.updateUser,
            "updateDate": self.updateDate
        }
    
    @staticmethod
    def from_dict(data):
        entity = Entity()
        entity.id = data.get("id", 0)
        entity.creationUser = data.get("creationUser", 0)
        entity.creationDate = data.get("creationDate", "")
        entity.updateUser = data.get("updateUser", 0)
        entity.updateDate = data.get("updateDate", "")
        return entity