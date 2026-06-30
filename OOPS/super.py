#super function
#used to call methods of parent class to the child class
#it is needed to prevent overriding, we have all the methods of the parent class in the child classes, but if we have constructor in both, it overrides the parent constructor
#it is also used to extend a method of the parent class
class shape():
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def og_method(self):
        print(f"This is of color {self.color} and it is {'filled' if self.is_filled else 'not filled'}") #the original method 1

class square(shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

class circle(shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class triangle(shape):
    def __init__(self, color, is_filled, side, height):
        super().__init__(color, is_filled)
        self.height = height
    
    def og_method(self): 
        print(f"This is a triangle of color {self.color}") #the method that will override the og one
        #super().og_method() #here super is used to extend the method that would have been overriden since they have the same name

square1 = square("red", True, 10)
circle1 = circle("blue", False, 5)
triangle1 = triangle("Green", False, 15, 20)

print(triangle1.color) #do same for square/circle 
print(triangle1.is_filled)
print(triangle1.height)
print(triangle1.og_method()) #output is Green
#                                   False
#                                   20
#                                   This is a triangle of color Green
#if we do:
"""
class triangle(shape):
    def __init__(self, color, is_filled, side, height):
        super().__init__(color, is_filled)
        self.height = height
    
    def og_method(self): 
        print(f"This is a triangle of color {self.color}")
        super().og_method()

then the output would have both print statements, no overriding
"""