#static methods are methods that do not need an object to be used, unlike instance methods

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_info(self): #instance method
        print(f"Name: {self.name}, Pos: {self.role}")

    @staticmethod 
    def is_valid_position(position): #static method
        valid_positions = ["Cashier", "Cook", "Janitor", "Manager"]
        return position in valid_positions

employee1 = Employee("Alex", "Manager")
employee1.get_info() #this is an instance method being used after we make an object

print(Employee.is_valid_position("Cook")) #static method being used, it is used directly by the class
print(Employee.is_valid_position("Theif"))