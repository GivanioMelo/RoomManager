class Entity:
    id: int
    creationUserId: int
    creationDate: str
    updateUserId: int
    updateDate: str

    def __init__(self, id=0, creationUser=0, creationDate="", updateUser=0, updateDate=""):
        self.id = id
        self.creationUserId = creationUser
        self.creationDate = creationDate
        self.updateUserId =  updateUser
        self.updateDate = updateDate
    
    def __str__(self):
        return f"Entity(id={self.id}, creationUser={self.creationUserId}, creationDate={self.creationDate}, updateUser={self.updateUserId}, updateDate={self.updateDate})"
    
    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            "id": self.id,
            "creationUser": self.creationUserId,
            "creationDate": self.creationDate,
            "updateUser": self.updateUserId,
            "updateDate": self.updateDate
        }
    
    @staticmethod
    def from_dict(data):
        entity = Entity()
        entity.id = data.get("id", 0)
        entity.creationUserId = data.get("creationUser", 0)
        entity.creationDate = data.get("creationDate", "")
        entity.updateUserId = data.get("updateUser", 0)
        entity.updateDate = data.get("updateDate", "")
        return entity