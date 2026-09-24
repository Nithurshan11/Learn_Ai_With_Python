"""
class Student

index_num = ""
name=""

def__init__()
def printStudData()

class ITStudent

subject=""

def __init()
def printItStudData()


class SWStudent

duraction=""
fees=0

def __init()
def printSWStudData()


"""


class Student:
    index_num = ""
    name = ""

    def __init__(self, index_num, name):
        self.index_num = index_num
        self.name = name

    def printStuData(self):
        print("Student Index Number :", self.index_num)
        print("Student Name :", self.name)


class ITStudent(Student):
    subject = ""

    def __init__(self, index_num, name, subject):
        super().__init__(index_num, name)
        self.subject = subject

    def printITStudData(self):
        super().printStuData()
        print("Subject :", self.subject)


class SWStudent(ITStudent):
    duration = ""
    fees = 0

    def __init__(self, index_num, name, subject, duration, fees):
        super().__init__(index_num, name, subject)
        self.duration = duration
        self.fees = fees

    def printSWStudData(self):
        super().printITStudData()
        print("Duration :", self.duration)
        print("Fees :", self.fees)


obj1 = SWStudent("001", "Mala", "IT", "4 Years", 5000)
obj1.printSWStudData()

print()

obj2 = SWStudent("002", "Nimal", "Software Engineering", "4 Years", 500000)
obj2.printSWStudData()














