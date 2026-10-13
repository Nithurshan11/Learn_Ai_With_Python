"""
class Employee

number=""
name = ""

def __init__()
def printEmpData()

class Manger

department = ""

def __init__()
def printManData()
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

    def __init__(self, number, name, department):
        super().__init__(number, name)
        self.department = department

    def printManData(self):
        super().printEmpData()
        print("Manager Department :", self.department)


obj1 = Manager("E001", "Nithurshan", "IT")
obj1.printManData()
        





        
        

