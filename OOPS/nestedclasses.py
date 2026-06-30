 #its a class defined inside another class
 #class outer:
    #class inner:

#reduces possibility of naming conflicts, allows to logically group classes that are closely related
class Company:
    class Employee:
        def __init__(self, name, role):
            self.name = name
            self.role = role

        #def show_details(self):
            #return f"Name: {self.name}, Position: {self.role}"

    def __init__(self, company_name):
        self.company_name = company_name 
        self.list = []
    
    def add_employee(self, name, role):
        new_employee = self.Employee(name, role)
        self.list.append(new_employee)

    def return_list(self):
        return [f"Name {x.name}, Role {x.role}" for x in self.list]
    

company = Company("Python. ltd")
company.add_employee("Alex", "CEO")
company.add_employee("Pirera", "New guy")
company.add_employee("Dana WHite", "Owner")

for x in company.return_list():
    print(x)
