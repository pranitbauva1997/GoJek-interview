from custom_exceptions import ParkingLotFull, ParkingLotUninitialized
from custom_exceptions import ParkingLotInvalidInputs

class ParkingLot:
    # Remember to +1 the index of vehicles while displaying the data
    # and -1 the index of vehicles while storing the data
    vehicles = None

    def __init__(self, size):
        if (size is None) or (not isinstance(size, int)) or (size < 1):
            raise ParkingLotInvalidInputs

        self.vehicles = [None] * size
        print('Created a parking lot with {} slots'.format(size))

    def add(self, car):
        slot = self.get_first_empty()
        if slot > len(self.vehicles) - 1:
            raise ParkingLotFull('Sorry, parking lot is full')

        self.vehicles[slot] = car
        return slot,  'Allocated slot number: {}'.format(slot + 1)

    def get_first_empty(self):
        i = 0

        if self is None or self.vehicles is None:
            raise ParkingLotUninitialized('Please initialize parking lot')

        for car in self.vehicles:
            if car is None:
                return i

            i = i + 1

        return i

    def leave(self, slot):
        car_left = self.vehicles[slot]
        self.vehicles[slot] = None
        car_left.slot = None
        return 'Slot number ' + str(slot + 1) + ' is free'

    def status(self):
        messages = []
        messages.append('{0:<10} {1:<20} {2:<10}'.format('Slot No.',
                                                         'Registration No',
                                                         'Colour'))
        for car in self.vehicles:
            if car is None:
                continue

            message = '{0:<10} {1:<20} {2:<10}'.format(car.slot + 1,
                                                       car.registration_no,
                                                       car.colour)
            messages.append(message)

        return messages

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

    def __str__(self):
        return ', '.join(self.vehicles)
