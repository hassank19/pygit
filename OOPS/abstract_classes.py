#abstract classes exit to serve as a blueprint with abstract methods that all child clASSES MUST FOLLOQ
from abc import ABC, abstractmethod #we need these for abstract class

class Vehicle(ABC): #our abstract class
    @abstractmethod
    def go(self): #we declare the methods but dont define them, thus pass
        pass

    @abstractmethod
    def stop(self):
        pass

#vehicle = Vehicle() #we cant make objects from abstract classes, it will show "Can't instantiate abstract class Vehicle with abstract methods go, stop"

class Car(Vehicle):
    def go(self):           #we have to define the methods of the abstract classes in the child classes, if you dont, you cant make objects ->TypeError
        print("The car is going")
    def stop(self):
        print("The car stopped")

class Moto(Vehicle):
    def go(self):
        print("The motorcyle is going")
    def stop(self):
        print("The motorcyle stopped")

car = Car()
car.go()
bike = Moto()
bike.stop()