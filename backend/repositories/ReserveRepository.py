import datetime
from repositories.BaseRepository import BaseRepository
from entities.Reserve import Reserve

class ReserveRepository(BaseRepository[Reserve]):
    def __init__(self):
        super().__init__()
        self.tableName = 'reserves'
    
    def create(self, reserve: Reserve) -> None:
        roomId = int(reserve.room)
        userId = int(reserve.reservedFor)
        startTime = reserve.startTime.strftime("%Y-%m-%d %H:%M:%S")
        endTime = reserve.endTime.strftime("%Y-%m-%d %H:%M:%S")
        creationUser = reserve.creationUser
        updateUser = reserve.updateUser

        query = f"INSERT INTO {self.tableName} (room, reservedFor, startDate, endDate, creationUser, updateUser) VALUES ({roomId}, {userId}, '{startTime}', '{endTime}',{creationUser},{updateUser})"
        print(f"Executing query: {query}")
        self.execute(query)


    def getReservesByRoom(self, room_id: int) -> list[Reserve]:
        query = f"SELECT * FROM {self.tableName} WHERE room_id = {room_id}"
        return self.executeQuery(query)
    
    def getRservesByUser(self, user_id: int) -> list[Reserve]:
        query = f"SELECT * FROM {self.tableName} WHERE user_id = ?"
        return self.executeQuery(query, (user_id,))
    
    def getReservesByRoomAndTime(self, room_id: int, start_time: datetime, end_time: datetime) -> list[Reserve]:
        start = start_time.strftime("%Y-%m-%d %H:%M:%S")
        end = end_time.strftime("%Y-%m-%d %H:%M:%S")

        query = f"""
        SELECT * FROM reserves WHERE room = {room_id} 
	    AND (
			(startDate >= '{start}' AND endDate <= '{end}') OR 
            (startDate <= '{start}' AND endDate >= '{end}') OR 
            (startDate <= '{start}' AND endDate >= '{start}' AND endDate <= '{end}') OR 
            (startDate >= '{start}' AND startDate <= '{end}' AND endDate >= '{end}')
		);
        """
        return self.executeQuery(query)