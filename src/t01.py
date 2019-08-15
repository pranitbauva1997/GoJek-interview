import unittest

from parking_lot       import ParkingLot
from car               import Car
from custom_exceptions import *

str_allocated_slot_number = 'Allocated slot number: {}'
str_status_raw            = '{0:10} {1:20} {2:10}'
str_leave                 = 'Slot number {} is free'

def prep_status_msg(slot_no, registration_no, colour):
    return str_status_raw.format(slot_no, registration_no, colour)

str_status_header = prep_status_msg('Slot No.', 'Registration No', 'Colour')

class TestParkingLotCarInternals(unittest.TestCase):

    def test_invalid_parking_lot_init(self):
        self.assertRaises(ParkingLotInvalidInputs, ParkingLot, None)
        self.assertRaises(ParkingLotInvalidInputs, ParkingLot, -1)
        self.assertRaises(ParkingLotInvalidInputs, ParkingLot, '1')
        self.assertRaises(ParkingLotInvalidInputs, ParkingLot, 1.1)

    def test_car_invalid_inputs(self):
        pk = ParkingLot(3)
        self.assertRaises(CarInvalidInputs,
                          Car.create_and_park, pk, None, None)
        self.assertRaises(CarInvalidInputs,
                          Car.create_and_park, pk, 'ABC', None)
        self.assertRaises(CarInvalidInputs,
                          Car.create_and_park, pk, None, 'White')

    def test_get_first_empty_barebones(self):
        pk = ParkingLot(3)
        self.assertEqual(0, pk.get_first_empty())
        pk.vehicles[2] = -1
        self.assertEqual(0, pk.get_first_empty())
        pk.vehicles[0] = -1
        self.assertEqual(1, pk.get_first_empty())
        pk.vehicles[1] = -1
        self.assertEqual(3, pk.get_first_empty())

    def test_pk_10_cars_barebones_valid(self):
        pk = ParkingLot(10)
        self.assertEqual([None]*10, pk.vehicles)
        self.assertEqual(10, len(pk.vehicles))
        self.assertNotEqual(None, len(pk.vehicles))

    def test_pk_10_cars_barebones_invalid(self):
        pk = ParkingLot(10)
        pk.vehicles[1] = 1
        self.assertNotEqual([None]*10, pk.vehicles)

    def test_pk_3_get_first_empty_barebones_valid(self):
        pk = ParkingLot(3)

        # Test for empty parking lot giving 0th index
        self.assertEqual(0, pk.get_first_empty())

        # Filling up the 0th index with a car
        pk.vehicles[0] = 1
        self.assertEqual(1, pk.get_first_empty())

        # Filling up the 1st index with a car
        pk.vehicles[1] = 2
        self.assertEqual(2, pk.get_first_empty())

        # Removing the car at 1st index from parking lot
        pk.vehicles[1] = None
        self.assertEqual(1, pk.get_first_empty())

        # Removing the car at 0th index from parking lot
        pk.vehicles[0] = None
        self.assertEqual(0, pk.get_first_empty())

    def test_pk_3_get_first_empty_overflow(self):
        pk = ParkingLot(3)
        self.assertEqual([None] * 3, pk.vehicles)
        car1, m1 = Car.create_and_park(pk, 'ABC', 'White')
        car2, m2 = Car.create_and_park(pk, 'MNO', 'Gray')
        car3, m3 = Car.create_and_park(pk, 'PQR', 'Black')

        self.assertEqual(3, pk.get_first_empty())
        self.assertRaises(ParkingLotFull,
                          Car.create_and_park, pk, 'XYZ', 'White')

    def test_pk_not_initialized(self):
        self.assertRaises(ParkingLotUninitialized,
                          Car.create_and_park, None, 'ABC', 'White')

    def test_pk_car_complete_valid(self):
        pk = ParkingLot(3)
        car, _ = Car.create_and_park(pk, 'ABC', 'White')

        self.assertEqual(car, pk.vehicles[car.slot])
        self.assertEqual(1, pk.get_first_empty())

        message = pk.leave(0)
        self.assertEqual(None, pk.vehicles[0])
        self.assertEqual('Slot number 1 is free', message)

class TestParkingLotCar(unittest.TestCase):
    @staticmethod
    def prepare_status():
        return [
            str_status_header,
            str_status_raw.format('1', 'ABC', 'White'),
            str_status_raw.format('2', 'MNO', 'Gray'),
            str_status_raw.format('3', 'PQR', 'Black'),
            str_status_raw.format('4', 'XYZ', 'White')
        ]
    def setUp(self):
        self.pk = ParkingLot(4)
        _, m1 = Car.create_and_park(self.pk, 'ABC', 'White')
        _, m2 = Car.create_and_park(self.pk, 'MNO', 'Gray')
        _, m3 = Car.create_and_park(self.pk, 'PQR', 'Black')
        _, m4 = Car.create_and_park(self.pk, 'XYZ', 'White')
        self.messages = [m1, m2, m3, m4]
        self.str_status = self.prepare_status()

    def test_allocated_slot_number_message(self):
        self.assertEquals(str_allocated_slot_number.format(1),
                          self.messages[0])
        self.assertEquals(str_allocated_slot_number.format(2),
                          self.messages[1])
        self.assertEquals(str_allocated_slot_number.format(3),
                          self.messages[2])
        self.assertEquals(str_allocated_slot_number.format(4),
                          self.messages[3])

    def test_status_message(self):
        messages = self.pk.status()
        self.assertEquals(self.str_status, messages)

    def test_registration_numbers_for_cars_with_colour(self):
        white_cars = self.pk.registration_numbers_for_cars_with_colour('White')
        self.assertEqual(['ABC', 'XYZ'], white_cars)
        self.assertNotEqual(['ABC', 'MNO'], white_cars)

    def test_slot_numbers_for_cars_with_colour(self):
        slot_numbers = self.pk.slot_numbers_for_cars_with_colour('White')
        self.assertEqual(['1', '4'], slot_numbers)
        self.assertNotEqual(['1', '3'], slot_numbers)

    def test_slot_numbers_for_registration_number(self):
        slot_numbers = self.pk.slot_number_for_registration_number('ABC')
        self.assertEqual('1', slot_numbers)

    def test_slot_numbers_for_registration_number_not_found(self):
        slot_numbers = self.pk.slot_number_for_registration_number('XXX')
        self.assertEqual('Not found', slot_numbers)

    def test_leave(self):
        message = self.pk.leave(1)
        self.assertEquals(str_leave.format(2), message)

    def test_already_left(self):
        message = self.pk.leave(1)
        self.assertRaises(ParkingSlotEmpty, self.pk.leave, 1)

if __name__ == '__main__':
    unittest.main()
