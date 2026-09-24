"""
Create a Python class called Employee with the following attributes:

Employee number
Employee name
Basic salary
Allowance
Gross salary

Use a parameterized constructor (__init__) to initialize the employee number, name, and basic salary.

Create setter methods to:

Calculate the allowance, which is 50% of the basic salary.
Calculate the gross salary using:
Gross Salary = Basic Salary + Allowance

Create getter methods to return each attribute.

Finally, create one Employee object and display all the employee details using the getter methods.
"""

class Employee:
    empnum = ""
    empname = ""
    salary = 0.0
    allowance = 0.0
    grossSalary = 0.0

    # Parameterized constructor
    def __init__(self, empnum, empname, salary):
        self.empnum = empnum
        self.empname = empname
        self.salary = salary

    # Setter to calculate allowance
    def setAllowance(self):
        self.allowance = self.salary * 50 / 100

    # Setter to calculate gross salary
    def setGrossSalary(self):
        self.grossSalary = self.salary + self.allowance

    # Getter methods
    def getNumber(self):
        return self.empnum

    def getName(self):
        return self.empname

    def getSalary(self):
        return self.salary

    def getAllowance(self):
        return self.allowance

    def getGrossSalary(self):
        return self.grossSalary


# Create employee object
obj1 = Employee("E001", "Nidurshan", 30000)

# Call setter methods
obj1.setAllowance()
obj1.setGrossSalary()

# Display employee details
print("Employee Number:", obj1.getNumber())
print("Employee Name:", obj1.getName())
print("Basic Salary:", obj1.getSalary())
print("Allowance:", obj1.getAllowance())
print("Gross Salary:", obj1.getGrossSalary())
