#has a 'owns a' relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheels:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power) #these are dependent on the engine and wheel classes, thus we call them compostion and not independent
        self.wheels = [Wheels(wheel_size) for x in range(4)]#we call the engine and wheel classes here to make an object like self.engine or self.wheels

    def display(self):
        return f"Car is of make {self.make} and of model {self.model}, with HP {self.engine.horse_power} and of wheel size {self.wheels[0].size}"
        #we cant jst do self.horse_power or self.size as they are attributes of engine and wheel classes, we have to go inside the classes using the '.' accessor 



car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=15)
# or car1 = Car("Ford", "Mustang", 500, 15)
print(car1.display())