from custom_exceptions import *

class Car:
    """A class used to represent the Car object

    This car object can be parked inside a ParkingLot. An attribute named
    `registration_no` is the unique property of the car.

    Attributes
    ----------
    colour          : str
        Major colour of the car used for identification
    registration_no : str
        Unique code issued to the car by the government
    slot            : str
        A spot in the parking lot

    Methods
    -------
    create_and_park(parking_lot, registration_no, colour)
        Creates a car object and parks it in the `parking_lot`
    park(parking_lot)
        Allocates a slot for the car in the parking lot (Do not use directly)
    """

    colour = None
    registration_no = None
    slot = None

    def __init__(self, registration_no, colour):
        """Default constructor

        Do not use directly. Instead call the `create_and_park()` method
        which initializes a new object and calls `park()` and also does
        exception handling.

        Parameters
        ----------
        registration_no : str
            Unique code issued to the car by the government
        color           : str
            Major colour of the car used for identification

        Returns
        -------
        message : str
            status message to be echoed in STDOUT

        Raises
        -------
        CarInvalidInputs
            If invalid inputs like no registration number or no colour
            are specified.
        """

        if registration_no is None or colour is None:
            raise CarInvalidInputs

        self.registration_no = registration_no
        self.colour = colour

    def park(self, parking_lot):
        """Parks the car in the `parking_lot`

        Do not use this directly. Instead prefer `create_and_park()`.

        Parameters
        ----------
        parking_lot : ParkingLot
            The `ParkingLot` object to which we want to add our car

        Returns
        ----------
        message : str
            status message to be echoed in STDOUT

        Raises
        ----------
        ParkingLotUnitialized
            If there are issues in creating a new parking not or trying
            to access a non-existent parking lot.
        ParkingLotFull
            If there is no space left in the parking lot for an extra
            car.
        ParkingSlotEmpty
            If for some serious reason `vehicles` attribute of parking_lot
            doesn't exist.
        """

        if len(parking_lot.vehicles) < 1:
            raise ParkingLotUninitialized('Please initialize parking lot')

        try:
            self.slot, message = parking_lot.add(self)
        except Exception as e:
            raise e

        return message

    @staticmethod
    def create_and_park(parking_lot, registration_no, colour):
        """Create and park a car

        This the recommended way of creating a new car and parking it
        in the parking lot.

        Parameters
        ----------
        parking_lot : ParkingLot
            The `ParkingLot` object to which we want to add our car
        registration_no : str
            Unique code issued to the car by the government
        color           : str
            Major colour of the car used for identification

        Returns
        ----------
        car     : Car
            The newly created car which is parked
        message : str
            status message to be echoed in STDOUT

        Raises
        ----------
        ParkingLotUninitialized
            If you try to add a car to a non-existent parking lot.
        ParkingLotFull
            If no slots available to park the new car.
        """

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
        """Readable string for debugging"""

        return '{0}. {1} {2}'.format(self.slot, self.registration_no,
                                     self.colour)
