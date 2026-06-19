class Car:
    def __init__(self, model, year, color, forSale):
        self.model = model
        self.year = year
        self.color = color
        self.forSale = forSale
    
    def drive(self):
        print(f"You are driving the car {self.model} of color {self.color}")
    
    def stop(self):
        print(f"You stopped the car of model {self.model} and of color {self.color}")