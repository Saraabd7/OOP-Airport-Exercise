class FlightTrip:

    def __init__(self, origin = '', destination = '', flightid = '', list_of_passenger = [], plane_number = ''):
        self.origin = origin
        self.destination = destination
        self.flight_id = flightid
        self.list_of_passenger = list_of_passenger
        self.plane_number = plane_number

flight1 = FlightTrip()
flight1.add_destination('London')
flight1.add_origin('NewYork')
flight1.add_plane('BA008')


flight2 = FlightTrip()
flight2.add_destination('Amsterdam')
flight2.add_origin('Istanbul')
flight2.add_plane('BA002')

flight3 = FlightTrip()
flight2.add_destination('Paris')
flight2.add_origin('Madrid')
flight2.add_plane('BA009')


list_flights = []
list_flights.append(flight1)
list_flights.append(flight2)
list_flights.append(flight3)

#Flight Trip class

# origin
# Destination
# list of passengers
# plane number

# need some getters nd setter:

# as a user I can add a plane
# as a User I can add a destination
# As a user I can add a origin

# As a user I can add a Passenger to the list of passengers