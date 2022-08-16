class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
            print("Total Employee %d" %Employee.empCount)

    def displayEmployee(self):
            print("Name: ", self.name, ", Salary: ", self.salary )
"this would create the first object of employee class"
emp1 = Employee("Luciah", 2000)
"this would create the second object of employee class"
emp2 = Employee("Jade", 100)
emp1.displayEmployee()
emp2.displayEmployee()
setattr(emp1,'age', 23)
print("Total employee %d" %Employee.empCount)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)


