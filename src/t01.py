import unittest
from parking_lot import ParkingLot
from car         import Car

class TestParkingLot(unittest.TestCase):

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
        car = Car.create_and_park(pk, "ABC", "White")

        self.assertEqual(car, pk.vehicles[car.slot])
        self.assertEqual(1, pk.get_first_empty())

        pk.eject(0)
        self.assertEqual(None, pk.vehicles[0])

    def test_registration_nos_for_cars_with_colour(self):
        pk = ParkingLot(4)
        Car.create_and_park(pk, "ABC", "White")
        Car.create_and_park(pk, "MNO", "Gray")
        Car.create_and_park(pk, "PQR", "Black")
        Car.create_and_park(pk, "XYZ", "White")

        white_cars = pk.registration_nos_for_cars_with_colour("White")
        self.assertEqual(["ABC", "XYZ"], white_cars)
        self.assertNotEqual(["ABC", "MNO"], white_cars)

        white_cars = pk.slots_for_cars_with_colour("White")
        self.assertEqual([1, 4], white_cars)
        self.assertNotEqual([1, 3], white_cars)

        white_cars = pk.slot_for_registration_number("ABC")
        self.assertEqual('1', white_cars)

        pk.eject(1)
        pk.status()


if __name__ == '__main__':
    unittest.main()
