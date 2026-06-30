from car import Car

car1 = Car("Nissan", 1998, "red", False)
car2 = Car("Toyota", 2000, "white", True)

#print(car1.model)
#print(car2.model)
#car1.stop()
#car1.describe()

print(f"{car1.model}")
print(f"{car2.model}")
print(f"{Car.country}") #we acces a class variable using the class' name
