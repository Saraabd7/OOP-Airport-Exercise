from Plane_class import *
from Passenger_class import *
from People_class import *
from Flight_Trip import *


plane_list = []
passenger_list = []
flight_list = []

while True:
    plane_number = input(' Enter the plane_number or enter exit to exit:\n')
    if 'exit' in plane_number:
        break
    else:
        cargo = input('Enter the cargo size:\n')
        plane = Plane(plane_number, cargo)
        plane_list.append(plane)

[print(i.plane_number, i.cargo) for i in plane_list]

while True:
    name = input('Enter the plane_number or enter exit to exit:\n')
    if 'exit' in plane_number:
        break
    else:
        passenger_number = input('Enter the cargo size:\n')
        passenger = Passenger(name, passenger_number)
        passenger_list.append(passenger)

[print(i.name, i.passenger_number) for i in passenger_list]


while True:
    user_input = input('Would you like to book flights? y/n')
    if user_input == 'yes':
        user_input = input('Would you like to enter your flight details? y/n')
    if user_input == 'yes':
        origin = input('Please enter the origin of the flight.')
        destination = input('Please enter the destination of the flight.')
        list_of_passengers = input('Please enter the list of passengers.')
        plane_number = input('Please input the plane number of the flight.')
        flight_id = len(flight_list)
        flight_trip = FlightTrip(origin, destination, flight_id, list_of_passengers, plane_number )
    elif user_input == 'no':
        flight_trip = FlightTrip()
    elif user_input == 'no':
        print('Thank you!')
        break

        # do the simplest SIMPLEST

        # switch board