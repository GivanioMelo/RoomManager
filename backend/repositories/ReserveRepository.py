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
				{reserve.roomId},
				{reserve.reservedForId},
				'{reserve.startDate.strftime('%Y-%m-%d %H:%M:%S')}',
				'{reserve.endDate.strftime('%Y-%m-%d %H:%M:%S')}',
				{reserve.creationUserId},
				{reserve.updateUserId});
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
				{reserve.roomId},
				{reserve.reservedForId},
				'{reserve.startDate.strftime("%Y-%m-%d %H:%M:%S")}',
				'{reserve.endDate.strftime("%Y-%m-%d %H:%M:%S")}',
				{reserve.creationUserId},
				{reserve.updateUserId}),
			"""
		query = query.rstrip(',') + ';'
		print(f"Executing query: {query}")

	def getReservesByRoom(self, room_id: int) -> list[Reserve]:
		query = f"SELECT * FROM {self.tableName} WHERE room = {room_id}"
		result = self.executeQuery(query)
		reserves = [Reserve.fromDict(record) for record in result]
		return reserves
	
	def getRservesByUser(self, user_id: int) -> list[Reserve]:
		query = f"SELECT * FROM {self.tableName} WHERE reservedFor = {user_id}"
		result = self.executeQuery(query)
		reserves = [Reserve.fromDict(record) for record in result]
		return reserves
	
	def getByRoomAndTime(self, roomId: int, startTime: datetime.datetime, endTime: datetime.datetime) -> list[Reserve]:
		start = startTime.strftime("%Y-%m-%d %H:%M:%S")
		end = endTime.strftime("%Y-%m-%d %H:%M:%S")

		query = f"""
		SELECT * FROM {self.tableName} WHERE room = {roomId} 
		AND (
			(startDate >= '{start}' AND endDate <= '{end}') OR 
			(startDate <= '{start}' AND endDate >= '{end}') OR 
			(startDate <= '{start}' AND endDate > '{start}' AND endDate <= '{end}') OR 
			(startDate >= '{start}' AND startDate < '{end}' AND endDate >= '{end}')
		);
		"""
		result = self.executeQuery(query)
		reserves = [Reserve.fromDict(record) for record in result]
		return reserves