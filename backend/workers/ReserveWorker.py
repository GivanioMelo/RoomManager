from datetime import datetime
from repositories.ReserveRepository import ReserveRepository
from repositories.RoomRepository import RoomRepository
from repositories.UserRepository import UserRepository
from entities.Reserve import Reserve

class ReserveWorker:
    def __init__(self):
        self.reserve_repository = ReserveRepository()
        self.room_repository = RoomRepository()
        self.user_repository = UserRepository()

    def create_reserve(self, room_id:int, user_id:int, start_time:datetime, end_time:datetime, creation_user:int=None, update_user:int=None) -> Reserve:
        reserve = Reserve(0, room_id, user_id, start_time, end_time, creation_user,update_user)
        valid, message = self.reserveIsValid(reserve)
        if not valid:
            return None, message
        if self.reserve_repository.getReservesByRoomAndTime(room_id, start_time, end_time):
            return None, "Room is already reserved for the specified time."
        
        return self.reserve_repository.create(reserve), "Reservation created successfully."

    def get_all_reserves(self):
        return self.reserve_repository.get_all()
    
    def getReservesByUser(self, user_id):
        reserves = self.reserve_repository.getRservesByUser(user_id)
        for reserve in reserves:
            reserve.roomData = self.room_repository.get_by_id(reserve.roomId)
        return reserves
    
    def get_reserves_by_room(self, room_id):
        reserves = self.reserve_repository.getReservesByRoom(room_id)
        for reserve in reserves:
            reserve.userData = self.user_repository.get_by_id(reserve.reservedForId)
        return 

    def get_reserve_by_room_and_time(self, room_id, start_time, end_time):
        return self.reserve_repository.getReservesByRoomAndTime(room_id, start_time, end_time)
    
    def reserveIsValid(self, reserve: Reserve) -> tuple[bool, str]:
        isValid = True
        message = "Reservation is valid"

        if not reserve.roomId or not reserve.reservedForId:
            isValid = False
            message = "Room and reservedFor cannot be empty"
        if not isinstance(reserve.roomId, int) or not isinstance(reserve.reservedForId, int):
            isValid = False
            message = "Room and reservedFor must be integers"
        if not isinstance(reserve.startDate, datetime) or not isinstance(reserve.endDate, datetime):
            isValid = False
            message = "Start time and end time must be datetime objects"
        if reserve.startDate >= reserve.endDate:
            isValid = False
            message = "Start time must be before end time"
        if reserve.startDate < datetime.now():
            isValid = False
            message = "Start time cannot be in the past"

        return isValid, message