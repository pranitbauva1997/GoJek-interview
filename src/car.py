from custom_exceptions import CarInvalidInputs
from custom_exceptions import ParkingLotFull, ParkingLotUninitialized

class Car:
    colour = None
    registration_no = None
    slot = None

    def __init__(self, registration_no, colour):
        if registration_no is None or colour is None:
            raise CarInvalidInputs

        self.registration_no = registration_no
        self.colour = colour

    def park(self, parking_lot):
        if len(parking_lot.vehicles) < 1:
            raise ParkingLotUninitialized('Please initialize parking lot')

        try:
            self.slot, message = parking_lot.add(self)
        except Exception as e:
            raise e

        return message

    @staticmethod
    def create_and_park(parking_lot, registration_no, colour):
        if parking_lot is None or parking_lot.vehicles is None:
            raise ParkingLotUninitialized('Please initialize parking lot')

        car = Car(registration_no, colour)
        try:
            message = car.park(parking_lot)
            return car, message

        except ParkingLotFull as e:
            raise e

        except Exception as e:
            return None, e

    def __str__(self):
        return '{0}. {1} {2}'.format(self.slot, self.registration_no,
                                     self.colour)
