"""
class Emlopyee

empn=""
empname=""

def __init__()
def printEmpData()

class Director             class Manager

profit =0.0                 deraprment=""
                             salary = 0

def__init__()                def__init__()
def printdata()              def printdta()
"""

class Employee:
    empn = ""
    empname = ""

    def __init__(self, empn, empname):
        self.empn = empn
        self.empname = empname

    def printEmpData(self):
        print("Employee Number:", self.empn)
        print("Employee Name:", self.empname)


class Director(Employee):
    profit = 0.0

    def __init__(self, empn, empname, profit):
        super().__init__(empn, empname)
        self.profit = profit

    def printDirData(self):
        super().printEmpData()
        print("Profit:", self.profit)


class Manager(Employee):
    department = ""
    salary = 0

    def __init__(self, empn, empname, department, salary):
        super().__init__(empn, empname)
        self.department = department
        self.salary = salary

    def printManData(self):
        super().printEmpData()
        print("Department:", self.department)
        print("Salary:", self.salary)


# Director object
obj1 = Director("E001", "Nithurshan", 50000)

print("Director Information")
obj1.printDirData()


# Manager object
obj2 = Manager("E002", "Kamal", "IT", 75000)

print("\nManager Information")
obj2.printManData()
