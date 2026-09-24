"""
Constructor Declaration
-------------------------

def__init__(Argument Variable List):

     -------;
     -------;

Ex
---
create the employee cls with attribute emp num , name and salary
use a parameter constructor to initialize emp details , Get method
to return each employee data . Make one object
"""

class Employee:
    def __init__(self, eno, ename, sal):
        self.empno = eno
        self.empname = ename
        self.salary = sal

    def getNumber(self):
        return self.empno

    def getName(self):
        return self.empname

    def getSalary(self):
        return self.salary


# Create one object
obj1 = Employee("1234", "Nidurshan", 30000)

# Get employee details
print("Employee Number:", obj1.getNumber())
print("Employee Name:", obj1.getName())
print("Salary:", obj1.getSalary())



