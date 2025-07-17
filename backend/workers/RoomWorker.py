from repositories.ReserveRepository import ReserveRepository
from repositories.UserRepository import UserRepository
from repositories.RoomRepository import RoomRepository
from entities.Room import Room
from entities.Reserve import Reserve

import datetime
from entities.User import User

class RoomWorker:
    def __init__(self):
        self.roomRepository = RoomRepository()
        self.reserveRepository = ReserveRepository()
        self.userRepository = UserRepository()

    def create(self, name: str, capacity: int) -> Room:
        room = Room(0, name, capacity)
        return self.roomRepository.create(room)

    def getAll(self) -> list[Room]:
        rooms = self.roomRepository.getAll()
        startTime = datetime.datetime.today()
        endTime = startTime + datetime.timedelta(hours=23,minutes=59)
        for room in rooms:
            room.reserves = self.reserveRepository.getByRoomAndTime(room.id,startTime,endTime)
            for reserve in room.reserves:
                reserve.userData = self.userRepository.getById(reserve.reservedForId)
        return rooms

    def getById(self, roomId: int) -> Room:
        return self.roomRepository.getById(roomId)

    def getByUserReservations(self, userId: int) -> list[Room]:
        return self.roomRepository.getByUserReservations(userId)
