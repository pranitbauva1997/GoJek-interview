class ParkingLot:
    # Remember to +1 the index of vehicles while displaying the data
    # and -1 the index of vehicles while storing the data
    vehicles = None

    def __init__(self, size):
        self.vehicles = [None] * size

    def add(self, car):
        slot = self.get_first_empty()
        self.vehicles[slot] = car
        print "Allocated slot number: " + str(slot + 1)
        return slot

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
        print "Slot number " + str(slot + 1) + " is free"
