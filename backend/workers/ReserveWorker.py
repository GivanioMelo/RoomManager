from repositories.ReserveRepository import ReserveRepository
from entities.Reserve import Reserve

class ReserveWorker:
    def __init__(self):
        self.reserve_repository = ReserveRepository()

    def create_reserve(self, room_id, user_id, start_time, end_time):
        reserve = Reserve(0, room_id, user_id, start_time, end_time, True)

        if self.reserve_repository.get_by_room_and_time(room_id, start_time, end_time): return None

        return self.reserve_repository.create(reserve)

    def get_all_reserves(self):
        return self.reserve_repository.get_all()
    
    def get_reserves_by_user(self, user_id):
        return self.reserve_repository.get_by_user(user_id)
    
    def get_reserves_by_room(self, room_id):
        return self.reserve_repository.get_by_room(room_id)

    def get_reserve_by_room_and_time(self, room_id, start_time, end_time):
        return self.reserve_repository.get_by_room_and_time(room_id, start_time, end_time)