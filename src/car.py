class Car:
    colour = None
    registration_no = None
    slot = None

    def __init__(self, registration_no, colour):
        # Raise an exception if no registration number or no colour
        self.registration_no = registration_no
        self.colour = colour

    def park(self, parking_lot):
        if len(parking_lot.vehicles) < 1:
            # Raise an exception
            pass

        self.slot, message = parking_lot.add(self)
        return message

    @staticmethod
    def create_and_park(parking_lot, registration_no, colour):
        car = Car(registration_no, colour)
        message = car.park(parking_lot)

        return car, message
