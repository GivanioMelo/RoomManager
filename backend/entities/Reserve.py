import datetime

from entities.Entity import Entity

class Reserve(Entity):
    def __init__(self, id: int, roomId, userId, startTime, endTime):
        super().__init__(id=id)
        self.room = roomId # Assuming roomId is an integer representing the room ID
        self.reservedFor = userId # Assuming userId is an integer representing the user ID
        self.startTime = startTime
        self.endTime = endTime

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
    
    def isValid(self) -> bool:
        dateFormat = "%Y-%m-%d %H:%M:%S"
        try:
            start = datetime.datetime.strptime(self.startTime, dateFormat)
            end = datetime.datetime.strptime(self.endTime, dateFormat)
        except ValueError: return False
        if start >= end: return False
        return True

    def colision(self, other: 'Reserve') -> bool:
        dateFormat = "%Y-%m-%d %H:%M:%S"
        st0 = datetime.datetime.strptime(self.startTime, dateFormat)
        st1 = datetime.datetime.strptime(other.startTime, dateFormat)
        et0 = datetime.datetime.strptime(self.endTime, dateFormat)
        et1 = datetime.datetime.strptime(other.endTime, dateFormat)

        if self.room != other.room: return False
        if et0 < st1 or et1 < st0: return False
        return (((st0 >= st1 and st0 <= et1) or (et0 >= st1 and et0 <= et1)))