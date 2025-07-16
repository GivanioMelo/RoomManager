from repositories.RoomRepository import RoomRepository
from entities.Room import Room
from datetime import datetime

class RoomWorker:
    def __init__(self):
        self.roomRepository = RoomRepository()

    def create_room(self, name: str, capacity: int) -> Room:
        room = Room(0, name, capacity)
        return self.roomRepository.create(room)

    def get_all_rooms(self) -> list[Room]:
        return self.roomRepository.getAll()

    def get_room_by_id(self, room_id: int) -> Room:
        return self.roomRepository.getById(room_id)

    def get_rooms_by_user_reservations(self, user_id: int) -> list[Room]:
        return self.roomRepository.getByUserReservations(user_id)
