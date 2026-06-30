#Inheritance allows a class to inherit methods and attributes from another class
#eg: class child(parent)

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def eat(self):
        print(f"{self.name} is eating")

    def how_old(self):
        print(f"{self.name} is {self.age} years old")

class Dog(Animal): 
    def speak(self): #this method is not inherited
        print(f"{self.name} is barking")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is Meowing")

#the class dog and cat inhertied methods from the class animal

dog = Dog("Scoobey", 18) #defining an object dog
cat = Cat("Meow", 9)
dog.eat()
dog.how_old()
cat.sleep()