"""
class Employee
-------------

number="";
name=""

def__init__()
def printEmpData()

class Manager
---------------

department=""
salary=0.0

def__init__()
def printManData()

class AssManager
----------------

bonus-0.0;
gross_salary=0.0

def__init()
def calSalary()
def printAssManData()

add 50% bonus to all assistant manager

"""

class Employee:
    number = ""
    name = ""

    def __init__(self, number, name):
        self.number = number
        self.name = name

    def printEmpData(self):
        print("Employee Number :", self.number)
        print("Employee Name :", self.name)


class Manager(Employee):
    department = ""
    salary = 0.0

    def __init__(self, number, name, department, salary):
        super().__init__(number, name)
        self.department = department
        self.salary = salary

    def printManData(self):
        super().printEmpData()
        print("department :", self.department)
        print("Salary :", self.salary)


class AssManager(Manager):
    bonus = 0.0
    gross_salary = 0.0

    def __init__(self, number, name, department, salary):
        super().__init__(number, name, department, salary)

    def calSalary(self):
        self.bonus = self.salary * 50 / 100
        self.gross_salary = self.salary + self.bonus

    def printAssManData(self):
        super().printManData()
        print("Bonus :", self.bonus)
        print("Gross Salary :", self.gross_salary)


obj1 = AssManager("E001", "Nithurshan", "It", 100000)

obj1.calSalary()
obj1.printAssManData()
