from datetime import datetime
from repositories.BaseRepository import BaseRepository
from entities.Room import Room

class RoomRepository(BaseRepository[Room]):
    def __init__(self):
        super().__init__()
        self.tableName = 'rooms'
    
    def create(self, room: Room) -> Room:
        query = f"""
            INSERT INTO {self.tableName} (name, capacity, creationUser, updateUser)
            VALUES ('{room.name}', {room.capacity}, {room.creationUserId}, {room.updateUserId});
        """
        print(f"Executing query: {query}")
        self.execute(query)
        room.id = self.get_last_insert_id()
        return room
    
    def createMany(self, rooms: list[Room]) -> None:
        query = f"""
            INSERT INTO {self.tableName} (name, capacity, creationUser, updateUser)
            VALUES
        """
        for room in rooms:
            query += f"('{room.name}', {room.capacity}, {room.creationUserId}, {room.updateUserId}),"
        query = query.rstrip(',') + ';'
        print(f"Executing query: {query}")
        self.execute(query)
    
    def getAll(self) -> list[Room]:
        query = f"SELECT * FROM {self.tableName}"
        return self.executeQuery(query)
    
    def getById(self, roomId: int) -> Room:
        query = f"SELECT * FROM {self.tableName} WHERE id = {roomId}"
        result = self.executeQuery(query)
        return result[0] if result else None
    
    def getByUserReservations(self, userId: int) -> list[Room]:
        query = f"""
            SELECT r.* FROM {self.tableName} r
            JOIN reserves res ON r.id = res.room
            WHERE res.reservedFor = {userId} AND res.endDate > '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}'
        """
        return self.executeQuery(query)