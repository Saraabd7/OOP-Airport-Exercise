from People_class import *

class Passenger(People):
    def __init__(self, name, passport_number):
        super().__init__(name)
        self.passport_number = passport_number

    def add_passport_number(self, passport_number):
        new_passenger_passport = self
        new_passenger_passport.passport_number.append(passport_number)

list_of_passengers = []


passenger1 = Passenger('Steve Cameron', 'B343123')
passenger2 = Passenger('James Williams', 'B578998')
passenger3 = Passenger('David Steve', 'B465745')
passenger4 = Passenger('John Smith', 'B7223344')
passenger5 = Passenger('Sara Baker', 'B765893')


list_of_passengers.append(passenger1)
list_of_passengers.append(passenger2)
list_of_passengers.append(passenger3)
list_of_passengers.append(passenger4)
list_of_passengers.append(passenger5)

# Passenger class
# inherits from people

# attributes:
# passport number