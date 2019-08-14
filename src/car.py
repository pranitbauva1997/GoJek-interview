class Car:
    color = None
    registration_no = None
    slot = None

    def __init__(self, registration_no, color):
        # Raise an exception if no registration number or no color
        self.registration_no = registration_no
        self.color = color

    def park(self, parking_lot):
        if len(parking_lot.vehicles) < 1:
            # Raise an exception
            pass

        self.slot = parking_lot.add(self)

    @staticmethod
    def create_and_park(parking_lot, registration_no, color):
        car = Car(registration_no, color)
        car.park(parking_lot)

        return car
