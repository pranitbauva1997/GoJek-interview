class ParkingLot:
    # Remember to +1 the index of vehicles while displaying the data
    # and -1 the index of vehicles while storing the data
    vehicles = None

    def __init__(self, size):
        self.vehicles = [None] * size
        print 'Created a parking lot with {} slots'.format(size)

    def add(self, car):
        slot = self.get_first_empty()
        if slot > len(self.vehicles) - 1 or slot is None:
            # Raise an exception here
            print 'Sorry, parking lot is full'
            return None

        self.vehicles[slot] = car
        print 'Allocated slot number: {}'.format(slot + 1)
        return slot

    def get_first_empty(self):
        i = 0

        # Raise initialization exception

        for car in self.vehicles:
            if car is None:
                return i

            i = i + 1

    def leave(self, slot):
        car_left = self.vehicles[slot]
        self.vehicles[slot] = None
        car_left.slot = None
        print "Slot number " + str(slot + 1) + " is free"

    def status(self):
        print '{0:<10} {1:<20} {2:<10}'.format('Slot No.', 'Registration No',
                                               'Colour')
        for car in self.vehicles:
            if car is None:
                continue

            print '{0:<10} {1:<20} {2:<10}'.format(car.slot + 1,
                                                   car.registration_no,
                                                   car.colour)

    def registration_numbers_for_cars_with_colour(self, colour):
        output = []
        for car in self.vehicles:
            if car.colour == colour:
                output.append(car.registration_no)

        return output

    def slot_numbers_for_cars_with_colour(self, colour):
        output = []
        for car in self.vehicles:
            if car.colour == colour:
                output.append(str(car.slot + 1))

        return output

    def slot_number_for_registration_number(self, registration_no):
        for car in self.vehicles:
            if car.registration_no == registration_no:
                return str(car.slot + 1)

        return 'Not found'
