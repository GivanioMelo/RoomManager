from repositories.ReserveRepository import ReserveRepository
from repositories.UserRepository import UserRepository
from repositories.RoomRepository import RoomRepository
from entities.Room import Room
from entities.Reserve import Reserve

from datetime import datetime
from entities.User import User

class RoomWorker:
    def __init__(self):
        self.roomRepository = RoomRepository()
        self.reserveRepository = ReserveRepository()
        self.userRepository = UserRepository()

    def create_room(self, name: str, capacity: int) -> Room:
        room = Room(0, name, capacity)
        return self.roomRepository.create(room)

    def get_all_rooms(self) -> list[Room]:
        rooms = self.roomRepository.getAll()
        for room in rooms:
            room.reserves = self.reserveRepository.getReservesByRoom(room_id=room.id)
            for reserve in room.reserves:
                reserve.userData = self.userRepository.getById(reserve.reservedForId)
        return rooms

    def get_room_by_id(self, room_id: int) -> Room:
        return self.roomRepository.getById(room_id)

    def get_rooms_by_user_reservations(self, user_id: int) -> list[Room]:
        return self.roomRepository.getByUserReservations(user_id)
