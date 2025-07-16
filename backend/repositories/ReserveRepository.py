import datetime
from repositories.BaseRepository import BaseRepository
from entities.Reserve import Reserve

class ReserveRepository(BaseRepository[Reserve]):
	def __init__(self):
		super().__init__()
		self.tableName = 'reserves'
	
	def create(self, reserve: Reserve) -> None:
		query = f"""
			INSERT INTO {self.tableName}
			(room, reservedFor, startDate, endDate, creationUser, updateUser)
			VALUES (
				{reserve.room},
				{reserve.reservedFor},
				'{reserve.startTime.strftime('%Y-%m-%d %H:%M:%S')}',
				'{reserve.endTime.strftime('%Y-%m-%d %H:%M:%S')}',
				{reserve.creationUser},
				{reserve.updateUser});
			"""
		
		print(f"Executing query: {query}")
		self.execute(query)

	def create_many(self, reserves: list[Reserve]) -> None:
		query = f"""
			INSERT INTO {self.tableName}
			(room, reservedFor, startDate, endDate, creationUser, updateUser)
			VALUES 
			"""
		for reserve in reserves:
			query += f"""
			(
				{reserve.room},
				{reserve.reservedFor},
				'{reserve.startTime.strftime("%Y-%m-%d %H:%M:%S")}',
				'{reserve.endTime.strftime("%Y-%m-%d %H:%M:%S")}',
				{reserve.creationUser},
				{reserve.updateUser}),
			"""
		query = query.rstrip(',') + ';'
		print(f"Executing query: {query}")

	def getReservesByRoom(self, room_id: int) -> list[Reserve]:
		query = f"SELECT * FROM {self.tableName} WHERE room_id = {room_id}"
		return self.executeQuery(query)
	
	def getRservesByUser(self, user_id: int) -> list[Reserve]:
		query = f"SELECT * FROM {self.tableName} WHERE user_id = {user_id}"
		return self.executeQuery(query)
	
	def getReservesByRoomAndTime(self, room_id: int, start_time: datetime, end_time: datetime) -> list[Reserve]:
		start = start_time.strftime("%Y-%m-%d %H:%M:%S")
		end = end_time.strftime("%Y-%m-%d %H:%M:%S")

		query = f"""
		SELECT * FROM {self.tableName} WHERE room = {room_id} 
		AND (
			(startDate >= '{start}' AND endDate <= '{end}') OR 
			(startDate <= '{start}' AND endDate >= '{end}') OR 
			(startDate <= '{start}' AND endDate >= '{start}' AND endDate <= '{end}') OR 
			(startDate >= '{start}' AND startDate <= '{end}' AND endDate >= '{end}')
		);
		"""
		return self.executeQuery(query)