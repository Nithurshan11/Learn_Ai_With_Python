"""
class Employee
number=""
name=""

def __init__()
def printEmpData()

class Manger

salary=0.0;
bonus=0.0
gross_sal=0.0;

def __init()
def salarycal()
def printManData()

bonus either 10% or 5% depend on salary
if salary above 100000 then 10%
otherwise 5%
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
    salary = 0.0
    bonus = 0.0
    gross_sal = 0.0

    def __init__(self, number, name, salary):
        super().__init__(number, name)
        self.salary = salary

    def salarycal(self):
        if self.salary > 100000:
            self.bonus = self.salary * 0.10
        else:
            self.bonus = self.salary * 0.05

        self.gross_sal = self.salary + self.bonus

    def printManData(self):
        super().printEmpData()
        print("Basic Salary :", self.salary)
        print("Bonus :", self.bonus)
        print("Gross Salary :", self.gross_sal)


obj1 = Manager("001", "Mala", 150000)

obj1.salarycal()
obj1.printManData()
