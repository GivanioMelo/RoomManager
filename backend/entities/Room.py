from entities.Entity import Entity

class Room(Entity):
    def __init__(self, id: str, name: str, description: str, capacity: int, location: str = ""):
        super().__init__(id)
        self.name = name
        self.description = description
        self.capacity = capacity
        self.location = location

        self.reserves = []  # Placeholder for reserves, to be populated later
        self.issues = []  # Placeholder for issues, to be populated later

    def __repr__(self):
        return f"Room(id={self.id}, name={self.name}, description={self.description}, capacity={self.capacity})"
    
    def __str__(self):
        return f"Room {self.name} (ID: {self.id}) - {self.description} (Capacity: {self.capacity})"
    
    def to_dict(self):
        dict_repr = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "capacity": self.capacity
        }
        if self.location: dict_repr["location"] = self.location
        if self.reserves: dict_repr["reserves"] = [reserve.to_dict() for reserve in self.reserves]
        if self.issues: dict_repr["issues"] = [issue.to_dict() for issue in self.issues]
        return dict_repr
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            capacity=data["capacity"]
        )