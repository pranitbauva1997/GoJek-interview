from custom_exceptions import *

class ParkingLot:
    """A class used to represent the Parking Lot object

    This parking lot object can have many parked cars inside it.

    Attributes
    ----------
    vehicles : [str]
        Array of car objects parked in their respective slots

    Methods
    ----------
    add(car)
        Add a car to the parking lot
    get_first_empty()
        Get the nearest empty slot to park a new car
    leave(slot)
        Let go of the car from the parking spot
    status()
        Show the slots, registration numbers and colour of the cars
        currently parked in the parking lot.
    registration_numbers_for_cars_with_colour(colour)
        Show the registration numbers of cars who's colour matches the
        parameter.
    slot_numbers_for_cars_with_colour(colour)
        Show the slot numbers of cars who's colour matches the parameter.
    slot_number_for_car_with_registration_number(registration_no)
        Show the slot number of the car with the given registration number.
    """

    # Remember to +1 the index of vehicles while displaying the data
    # and -1 the index of vehicles while storing the data
    vehicles = None

    def __init__(self, size):
        """Default Constructor"""
        if (size is None) or (not isinstance(size, int)) or (size < 1):
            raise ParkingLotInvalidInputs

        self.vehicles = [None] * size
        print('Created a parking lot with {} slots'.format(size))

    def add(self, car):
        """Add a car object to the parking lot

        This method is internally called by `create_and_park()` and should
        be avoided being called directly.

        Parameters
        ----------
        car : Car
            The car object to be parked

        Returns
        ----------
        slot   : int
            The slot allocated after parking
        message : str
            status message to be echoed in STDOUT

        Raises
        ----------
        ParkingLotFull
            If there is no space left in the parking lot for an extra car.
        """

        slot = self.get_first_empty()
        if slot > len(self.vehicles) - 1:
            raise ParkingLotFull('Sorry, parking lot is full')

        self.vehicles[slot] = car
        return slot,  'Allocated slot number: {}'.format(slot + 1)

    def get_first_empty(self):
        """Get the nearest empty slot to park a new car

        Internal method. Not be called from outside.

        Returns
        ----------
        slot : int
            the next free slot available for parking

        Raises
        ----------
        ParkingLotUninitialized
        """

        i = 0

        if self is None or self.vehicles is None:
            raise ParkingLotUninitialized

        for car in self.vehicles:
            if car is None:
                return i

            i = i + 1

        return i

    def leave(self, slot):
        """Let go of the car from the parking spot

        The car object is now discarded and the spot on parking lot is
        marked empty for the new car.

        Returns
        ----------
        message : str
            status message to be echoed in STDOUT

        Raises
        ----------
        ParkingSlotEmpty
            If for some serious reason `vehicles` attribute of parking lot
            doesn't exist.
        """

        if self.vehicles[slot] is None:
            raise ParkingSlotEmpty

        car_left = self.vehicles[slot]
        self.vehicles[slot] = None
        car_left.slot = None
        return 'Slot number ' + str(slot + 1) + ' is free'

    def status(self):
        """Show the summary of the parking lot with car details"""

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
        """Show registration numbers for cars of the specified colour"""

        output = []
        for car in self.vehicles:
            if car.colour == colour:
                output.append(car.registration_no)

        return output

    def slot_numbers_for_cars_with_colour(self, colour):
        """Show the slot numbers for cars of the specified colour"""
        output = []
        for car in self.vehicles:
            if car.colour == colour:
                output.append(str(car.slot + 1))

        return output

    def slot_number_for_registration_number(self, registration_no):
        """Show the slot number for car with a registration number"""
        for car in self.vehicles:
            if car.registration_no == registration_no:
                return str(car.slot + 1)

        return 'Not found'

    def __str__(self):
        """Readable string for debugging"""
        return ', '.join(self.vehicles)
