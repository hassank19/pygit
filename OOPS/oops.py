from car import Car

car1 = Car("Nissan", 1998, "red", False)
car2 = Car("Toyota", 2000, "white", True)

print(car1.model)
print(car2.model)
car1.stop()
car2.drive()