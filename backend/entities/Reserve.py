import datetime

from entities.Entity import Entity

class Reserve(Entity):
    def __init__(self, id: int, roomId:int, reservedForId:int, startDate:datetime, endDate:datetime, creationUserId:int=None, updateUserId:int=None):
        super().__init__(id=id)
        self.roomId = roomId # Assuming roomId is an integer representing the room ID
        self.reservedForId = reservedForId # Assuming userId is an integer representing the user ID
        self.startDate = startDate
        self.endDate = endDate
        self.creationUserId = creationUserId
        self.updateUserId = updateUserId

        self.roomData = None  # Placeholder for room data, to be populated later
        self.userData = None  # Placeholder for user data, to be populated later
        self.creationUserData = None  # Placeholder for creation user data, to be populated later
        self.updateUserData = None  # Placeholder for update user data, to be populated later

    def __repr__(self):
        return f"Reserve(id={self.id}, roomId={self.roomId}, userId={self.reservedForId}, startTime={self.startDate}, endTime={self.endDate})"
    
    def __str__(self):
        return f"Reserve {self.id} - Room: {self.roomId}, User: {self.reservedForId}, Start: {self.startDate}, End: {self.endDate}"
    
    def toDict(self):
        dict_repr = {
            "id": self.id,
            "roomId": self.roomId,
            "reservedForId": self.reservedForId,
            "startTime": self.startDate,
            "endTime": self.endDate
        }
        if self.roomData: dict_repr["roomData"] = self.roomData.toDict()
        if self.userData: dict_repr["userData"] = self.userData.toDict()
        if self.creationUserData: dict_repr["creationUserData"] = self.creationUserData.toDict()
        if self.updateUserData: dict_repr["updateUserData"] = self.updateUserData.toDict()
        return dict_repr
    
    @classmethod
    def fromDict(cls, data: dict):
        return cls(
            id=data["id"],
            roomId=data["room"],
            reservedForId=data["reservedFor"],
            startDate=data["startDate"],
            endDate=data["endDate"]
        )