#class methods, these work with the class itself, rather than the object


#self is used for working with objects but in class methods, cls is used to work with the classes themselves

class students:

    count = 0
    total_gpa = 0


    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        students.count += 1
        students.total_gpa = students.total_gpa + gpa

    @classmethod
    def total_count(cls):
        return f"Total count is {cls.count}"
    
    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa is {cls.total_gpa / cls.count}"

student1 = students("Alex", 5)
student2 = students("Steve", 10)
student3 = students("Diana", 15)

print(students.total_count())
print(students.average_gpa())