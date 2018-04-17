from _datetime import datetime


class FancyString(object):
    def __init__(self, string):
        self.x = string

    def make_question(self):
        return f'{self.x}?'


my_string = FancyString('Hi Sara')

print(my_string.make_question())


class Vehicle(object):
    num_wheels = None


class Car(Vehicle):
    num_wheels = 4


class Bicycle(Vehicle):
    num_wheels = 2

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        self.age = datetime.now().year - self.year

    def repair(self):
        if self.brand == "Brody":
            return 'send to brody shop'
        elif self.age > 20:
            return 'send to dumpster'
        elif self.num_wheels == 2:
            return "I have 2 wheels"
        else:
            return 'sell on craigslist'


ursula = Bicycle('Univega', 'orange', 2000)
saras_bike = Bicycle('Brody', 'black', 1900)

print(ursula.repair)
print(f'Ursula is {ursula.age} years old')
if saras_bike.age > ursula.age:
    print("Sara's bike is {} years older".format(saras_bike.age, ursula.age))

print(type(saras_bike))


def add(n1, n2):
    return n1 + n2


class Number(object):
    def __init__(self, num):
        self.num = num

    def add(self, other_number):
        return self.num + other_number


# Rainfall event (in past)
## mm of water
## volume
## number of hours dry before event
## number of hours dry after event
## intensity
## duration
## date, time
## location
## season
## available capacity
### event.calc_required_capacity()

# Rainfall forecast
## mm of water
## confidence
## temperature
## duration
## date, time
## location
## season

# Rain Barrel
## current_volume
## discharge rate
## capacity
## depth
## status
## colour
## is_bedazzled
## name
## location
### barrel.determine_action(forecast, last_event)

# Operating protocol (when to open, when to close)
# Based on predictions, should it open or close
