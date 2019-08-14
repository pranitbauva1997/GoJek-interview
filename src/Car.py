class Car:
    color = None
    registration_no = None
    slot = None

    def __init__(self, registration_no, color):
        # Raise an exception if no registration number or no color
        self.registration_no = registration_no
        self.color = color

    def assign_slot(self, parking_lot):
        pass

