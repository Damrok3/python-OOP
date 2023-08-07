# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does no have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive this car")
    def stop(self):
        print("this car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle")
    def stop(self):
        print("this motorcycle is stopped")

# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()