from entities.Entity import Entity

class Issue(Entity):
    def __init__(self, id, title, description, status):
        super().__init__(id)
        self.title = title
        self.description = description
        self.status = status

    def toDict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def fromDict(cls, data):
        return cls(
            issue_id=data.get('id'),
            title=data.get('title'),
            description=data.get('description'),
            status=data.get('status'),
            created_at=data.get('created_at'),
            updated_at=data.get('updated_at')
        )