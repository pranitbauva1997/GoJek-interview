class ParkingLot:
    size = None
    vehicles = None

    def __init__(self, size):
        self.size = size
        self.vehicles = [None] * size

    def add(self, car):
        self.vehicles[self.get_first_empty()] = car

    def get_first_empty(self):
        i = 0
        for car in self.vehicles:
            if car is None:
                return i

            i = i + 1

    def eject(self, slot):
        car_ejected = self.vehicles[slot]
        self.vehicles[slot] = None
        car_ejected.slot = None
