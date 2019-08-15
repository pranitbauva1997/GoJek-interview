import unittest
from parking_lot import ParkingLot
from car         import Car

class TestParkingLotCar(unittest.TestCase):

    def test_pk_10_cars_valid(self):
        pk = ParkingLot(10)
        self.assertEqual([None]*10, pk.vehicles)
        self.assertEqual(10, len(pk.vehicles))
        self.assertNotEqual(None, len(pk.vehicles))

    def test_pk_10_cars_invalid(self):
        pk = ParkingLot(10)
        pk.vehicles[1] = 1
        self.assertNotEqual([None]*10, pk.vehicles)

    def test_pk_3_get_first_empty_valid(self):
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

    def test_pk_car_complete_valid(self):
        pk = ParkingLot(3)
        car, _ = Car.create_and_park(pk, "ABC", "White")

        self.assertEqual(car, pk.vehicles[car.slot])
        self.assertEqual(1, pk.get_first_empty())

        pk.leave(0)
        self.assertEqual(None, pk.vehicles[0])

class TestParkingLotCarOperations(unittest.TestCase):
    def setUp(self):
        self.pk = ParkingLot(4)
        _, m1 = Car.create_and_park(self.pk, "ABC", "White")
        _, m2 = Car.create_and_park(self.pk, "MNO", "Gray")
        _, m3 = Car.create_and_park(self.pk, "PQR", "Black")
        _, m4 = Car.create_and_park(self.pk, "XYZ", "White")
        self.messages = [m1, m2, m3, m4]

    def test_registration_numbers_for_cars_with_colour(self):
        white_cars = self.pk.registration_numbers_for_cars_with_colour("White")
        self.assertEqual(["ABC", "XYZ"], white_cars)
        self.assertNotEqual(["ABC", "MNO"], white_cars)

    def test_slot_numbers_for_cars_with_colour(self):
        white_cars = self.pk.slot_numbers_for_cars_with_colour("White")
        self.assertEqual(['1', '4'], white_cars)
        self.assertNotEqual(['1', '3'], white_cars)

    def test_slot_numbers_for_registration_number(self):
        white_cars = self.pk.slot_number_for_registration_number("ABC")
        self.assertEqual('1', white_cars)

        self.pk.leave(1)
        self.pk.status()


if __name__ == '__main__':
    unittest.main()
