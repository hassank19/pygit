"""
@property = Decorator used to define a method as a property (it can be accesed like an attribute)
Benefit: Add additional logic when read, write or delete
Gives us a getter, setter and deleter method
"""

class Rectangle:
    def __init__(self, width, height):
        self._width = width #by writing _ we treat them as private internal attribute, they are not supposed to be accesed outside the class
        self._height = height

    @property
    def width(self): #getter method
        return f"Width is {self._width}cm" #ex here, _width and _height are supposed to be accesed only inside the class
    
    @property
    def height(self): ##getter method
        return f"Height is {self._height}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            print("Width must be greater than 0")
        else:
            self._width = new_width #notice how we are using the _width and _height internally of the class

    @height.setter
    def height(self, new_height):
        if new_height <= 0:
            print("height must be greater than 0")
        else:
            self._height = new_height

    @width.deleter
    def width(self):
        print(f"Width of {self._width}cm has been deleted")
        del self._width
    
    @height.deleter
    def height(self):
        print(f"Height of {self._height}cm has been deleted")
        del self._height
    
rectangle = Rectangle(10, 15)
print(rectangle.width)
print(rectangle.height)
#print(rectangle._height) 
#print(rectangle._width) #this would return just 10 and 15
rectangle.height = 5
rectangle.width = 5
print(rectangle.width)
print(rectangle.height)
#if rectangle.height = 0 it will return the statement that it should be greater than 0
del rectangle.width
del rectangle.height 