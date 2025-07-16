import datetime

from entities.Entity import Entity

class Reserve(Entity):
    def __init__(self, id: int, roomId:int, userId:int, startTime:datetime, endTime:datetime, creationUser:int=None, updateUser:int=None):
        super().__init__(id=id)
        self.room = roomId # Assuming roomId is an integer representing the room ID
        self.reservedFor = userId # Assuming userId is an integer representing the user ID
        self.startTime = startTime
        self.endTime = endTime
        self.creationUser = creationUser
        self.updateUser = updateUser

    def __repr__(self):
        return f"Reserve(id={self.id}, roomId={self.room}, userId={self.reservedFor}, startTime={self.startTime}, endTime={self.endTime})"
    
    def __str__(self):
        return f"Reserve {self.id} - Room: {self.room}, User: {self.reservedFor}, Start: {self.startTime}, End: {self.endTime}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "roomId": self.room,
            "userId": self.reservedFor,
            "startTime": self.startTime,
            "endTime": self.endTime
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            roomId=data["roomId"],
            userId=data["userId"],
            startTime=data["startTime"],
            endTime=data["endTime"]
        )