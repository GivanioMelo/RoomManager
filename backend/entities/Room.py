from entities.Entity import Entity

class Room(Entity):
    def __init__(self, id: str, name: str, description: str, capacity: int):
        super().__init__(id)
        self.name = name
        self.description = description
        self.capacity = capacity

    def __repr__(self):
        return f"Room(id={self.id}, name={self.name}, description={self.description}, capacity={self.capacity})"
    
    def __str__(self):
        return f"Room {self.name} (ID: {self.id}) - {self.description} (Capacity: {self.capacity})"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "capacity": self.capacity
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            capacity=data["capacity"]
        )