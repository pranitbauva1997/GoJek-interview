import sys

from parking_lot import ParkingLot
from car         import Car

pk = None

line_str = raw_input('')

try:
    while line_str != None:
        line = line_str.split(' ')

        if   line[0] == 'create_parking_lot':
            pk = ParkingLot(int(line[1]))
        elif line[0] == 'park':
            try:
                _, message = Car.create_and_park(pk, line[1], line[2])
                print(message)
            except Exception as e:
                print(e)
        elif line[0] == 'leave':
            try:
                message = pk.leave(int(line[1]) - 1)
                print(message)
            except Exception as e:
                print(e)
        elif line[0] == 'status':
            messages = pk.status()
            for message in messages:
                print(message)
        elif line[0] == 'registration_numbers_for_cars_with_colour':
            arr = pk.registration_numbers_for_cars_with_colour(line[1])
            print(', '.join(arr))
        elif line[0] == 'slot_numbers_for_cars_with_colour':
            arr = pk.slot_numbers_for_cars_with_colour(line[1])
            print(', '.join(arr))
        elif line[0] == 'slot_number_for_registration_number':
            print(pk.slot_number_for_registration_number(line[1]))

        line_str = raw_input('')

except EOFError:
    sys.exit(0)
except Exception as e:
    print(e)
