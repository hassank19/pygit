class Car:

    country = "USA" #class variables
    num = 0

    def __init__(self, model, year, color, forSale):
        self.model = model #instance variables
        self.year = year
        self.color = color
        self.forSale = forSale
        Car.num += 1 #we access the class variable and increment, this counts all 
    
    def drive(self): #these are called instance methods->methods that belong to individual objects created from that class, here Car
        print(f"You are driving the car {self.model} of color {self.color}")
    
    def stop(self):
        print(f"You stopped the car of model {self.model} and of color {self.color}")

    def describe(self):
        print(f"COlor : {self.color}, model :  {self.model}, year : {self.year}")