from entities.Issue import Issue
from entities.Reserve import Reserve
from entities.Entity import Entity

class Room(Entity):
    issues:list[Issue]
    reserves:list[Reserve]
    
    def __init__(self, id: str, name: str, description: str, capacity: int, location: str = "", color:str="#88888888"):
        super().__init__(id)
        self.name = name
        self.description = description
        self.capacity = capacity
        self.location = location
        self.color = color
        self.reserves = []  # Placeholder for reserves, to be populated later
        self.issues = []  # Placeholder for issues, to be populated later

    def __repr__(self):
        return f"Room(id={self.id}, name={self.name}, description={self.description}, capacity={self.capacity})"
    
    def __str__(self):
        return f"Room {self.name} (ID: {self.id}) - {self.description} (Capacity: {self.capacity})"
    
    def toDict(self):
        dict_repr = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "capacity": self.capacity,
            "color": self.color
        }
        if self.location: dict_repr["location"] = self.location
        if self.reserves: dict_repr["reserves"] = [reserve.toDict() for reserve in self.reserves]
        if self.issues: dict_repr["issues"] = [issue.toDict() for issue in self.issues]
        # print(dict_repr)
        return dict_repr
    
    @classmethod
    def fromDict(cls, data: dict):
        # print(data)
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            capacity=data["capacity"],
            location=data["location"],
            color = data["color"]
        )