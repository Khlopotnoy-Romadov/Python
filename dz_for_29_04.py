class Hotel:
    def __init__(self, num_rooms):
        nums_rooms = [0 for i in range(num_rooms)]
        self._rooms = {"SGL": nums_rooms[:],"DBL": nums_rooms[:],"Junior Suite": nums_rooms[:], "Suite": nums_rooms[:]}  # информация о статусе номеров
        self._prices = {"SGL": "1 rub", "DBL": "2 rub", "Junior Suite": "3 rub", "Suite": "4 rub"}
    def occypy(self, room_type,room_id):
        self._rooms[room_type][room_id] = 1

    def free(self, room_type, room_id):
        self._rooms[room_type][room_id] = 0

    def get_prices(self):
        return self._prices

hotel = Hotel(5)
print(hotel.get_prices())
print(hotel._rooms)
hotel.occypy("SGL", 3)
hotel.occypy("Suite", 0)
print(hotel._rooms)
hotel.free("SGL", 3)
hotel.free("Suite", 0)
print(hotel._rooms)


