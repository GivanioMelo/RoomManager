from repositories.BaseRepository import BaseRepository
from entities.Room import Room

class RoomRepository(BaseRepository[Room]):
    def __init__(self):
        super().__init__()
        self.tableName = 'rooms'