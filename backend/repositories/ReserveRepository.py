from repositories.BaseRepository import BaseRepository
from entities.Reserve import Reserve

class ReserveRepository(BaseRepository[Reserve]):
    def __init__(self):
        super().__init__()
        self.tableName = 'reserves'
    
    def get_reserves_by_room_id(self, room_id: int) -> list[Reserve]:
        query = f"SELECT * FROM {self.tableName} WHERE room_id = {room_id}"
        return self.execute_query(query)
    
    def get_reserves_by_user_id(self, user_id: int) -> list[Reserve]:
        query = f"SELECT * FROM {self.tableName} WHERE user_id = ?"
        return self.execute_query(query, (user_id,))