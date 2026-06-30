#its when an object has multiple forms
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
       return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base
    
    def area(self):
        return 0.5 * self.height * self.base

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)


#object1 = Class() is how we make an object, here we did same in the list
shapes = [Square(5), Circle(10), Triangle(10, 2), Pizza("Sausage", 15)] #a square is a square as well as a shape, same for the other 2
#pizza is a circle as well as a shape, thus polymorphism

for shape in shapes:
    print(f"{shape.area()}cm^2")