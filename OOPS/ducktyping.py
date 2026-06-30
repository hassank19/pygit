#Duck typing is a Python concept where an object's behavior matters more than its type.
#"If it walks like a duck and quacks like a duck, it's probably a duck."

class Animal():
    is_alive = True

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Robot():
    def speak(self):
        print("Beep Beep")

animals = [Dog(), Cat(), Robot()]
for animal in animals:
    animal.speak()

#robot is not an animal, but it has all the necessary attributes or methods of other objects, so it shows the form of an animal as well