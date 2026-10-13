"""
class Student

index_num = ""
subject=""

def__init__()
def printStudData()

class itStudent

mar1=0;
mar2=0;
mar3=0;
total=0;
avg=0.0;

def __init()
def markscal()
def printItStudData()

"""

class Student:
    index_num = ""
    name = ""
    subject = ""

    def __init__(self, index_num, name, subject):
        self.index_num = index_num
        self.name = name
        self.subject = subject

    def printStuData(self):
        print("Student Index Number :", self.index_num)
        print("Student Name :", self.name)
        print("Subject :", self.subject)


class ItStudent(Student):
    mar1 = 0
    mar2 = 0
    mar3 = 0
    total = 0
    avg = 0.0

    def __init__(self, index_num, name, subject, mar1, mar2, mar3):
        super().__init__(index_num, name, subject)

        self.mar1 = mar1
        self.mar2 = mar2
        self.mar3 = mar3

    def markscal(self):
        self.total = self.mar1 + self.mar2 + self.mar3
        self.avg = self.total / 3

    def printItStudentData(self):
        super().printStuData()

        print("Marks 1 :", self.mar1)
        print("Marks 2 :", self.mar2)
        print("Marks 3 :", self.mar3)
        print("Total :", self.total)
        print("Average :", self.avg)


obj1 = ItStudent("001", "Mala", "IT", 50, 70, 90)

obj1.markscal()
obj1.printItStudentData()

        


