#multiple inhertiance and multilevel inheritance

class animal(): #the grandparent class

    def __init__(self, name): #we can give the name attribute in constructor of the grand class so all the children classes can inherit from it
        self.name = name

    def eat(self):
        print(f"The {self.name} is eating")
    def sleep(self):
        print(f"The {self.name} is sleeping")
#----------------
class pred(animal): #parent classes
    def hunt(self):
        print(f"The {self.name} is hunting")
    
class prey(animal):
    def flee(self):
        print(f"The {self.name} is fleeing")
#----------------
class rabbit(prey): #child classes
    pass
class fish(pred, prey): #multi level inheritance
    pass
class tiger(pred):
    pass

bunny = rabbit("Bnuuy")
tiger1 = tiger("Bengal Tiger")
salmon = fish("Nemo")


bunny.flee()
tiger1.hunt()
salmon.flee() #fish inhertied from both classes so it has both
salmon.hunt()
tiger1.eat() #child class got method from the grandparent class