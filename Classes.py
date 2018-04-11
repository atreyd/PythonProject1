class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount = Employee.empCount + 1

    def displayCount(self):
        print("Total Employees %d " % Employee.empCount)

    def displayEmployee(self):
        print(" Name: ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Deepak", 6000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total number of Employess: %d" %Employee.empCount)