import datetime

from entities.Entity import Entity

class Reserve(Entity):
    def __init__(self, id: int, roomId:int, userId:int, startTime:datetime, endTime:datetime, creationUserId:int=None, updateUserId:int=None):
        super().__init__(id=id)
        self.roomId = roomId # Assuming roomId is an integer representing the room ID
        self.reservedForId = userId # Assuming userId is an integer representing the user ID
        self.startTime = startTime
        self.endTime = endTime
        self.creationUserId = creationUserId
        self.updateUserId = updateUserId

        self.roomData = None  # Placeholder for room data, to be populated later
        self.userData = None  # Placeholder for user data, to be populated later
        self.creationUserData = None  # Placeholder for creation user data, to be populated later
        self.updateUserData = None  # Placeholder for update user data, to be populated later

    def __repr__(self):
        return f"Reserve(id={self.id}, roomId={self.roomId}, userId={self.reservedForId}, startTime={self.startTime}, endTime={self.endTime})"
    
    def __str__(self):
        return f"Reserve {self.id} - Room: {self.roomId}, User: {self.reservedForId}, Start: {self.startTime}, End: {self.endTime}"
    
    def to_dict(self):
        dict_repr = {
            "id": self.id,
            "roomId": self.roomId,
            "userId": self.reservedForId,
            "startTime": self.startTime,
            "endTime": self.endTime
        }
        if self.roomData: dict_repr["roomData"] = self.roomData.to_dict()
        if self.userData: dict_repr["userData"] = self.userData.to_dict()
        if self.creationUserData: dict_repr["creationUserData"] = self.creationUserData.to_dict()
        if self.updateUserData: dict_repr["updateUserData"] = self.updateUserData.to_dict()
        return dict_repr
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            roomId=data["roomId"],
            userId=data["userId"],
            startTime=data["startTime"],
            endTime=data["endTime"]
        )