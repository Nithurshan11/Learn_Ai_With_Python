"""
class Student
-------------

id="";
name=""

def__init__()
def printStudData()

class SwStudent
---------------

duration=""
fee=0.0

def__init__()
def printItStudentData()

class ItStudent
----------------

mar1=0 , mar2=0 , mar3 = 0
total =0 , avg = 0.0

def__init()
def calMarks()
def printStudData()

"""
class Student:
    id = ""
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printStudData(self):
        print(" ID :", self.id)
        print(" Name :", self.name)


class SwStudent(Student):
    duration = ""
    fee = 0.0

    def __init__(self, id, name, duration, fee):
        super().__init__(id, name)
        self.duration = duration
        self.fee = fee

    def printItStudentData(self):
        super().printStudData()
        print("Duration :", self.duration)
        print("Fee :", self.fee)


class ItStudent(SwStudent):
    mar1 = 0
    mar2 = 0
    mar3 = 0
    total = 0
    avg = 0.0

    def __init__(self, id, name, duration, fee, mar1, mar2, mar3):
        super().__init__(id, name, duration, fee)
        self.mar1 = mar1
        self.mar2 = mar2
        self.mar3 = mar3

    def calMarks(self):
        self.total = self.mar1 + self.mar2 + self.mar3
        self.avg = self.total / 3

    def printStudData(self):
        super().printItStudentData()
        print("Mark 1 :", self.mar1)
        print("Mark 2 :", self.mar2)
        print("Mark 3 :", self.mar3)
        print("Total :", self.total)
        print("Average :", self.avg)


obj1 = ItStudent("S001", "Nithurshan", "4 Years", 500000, 80, 75, 90)

obj1.calMarks()
obj1.printStudData()





















