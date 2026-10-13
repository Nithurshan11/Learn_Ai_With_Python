class Student:
    number = ""
    name = ""

    def __init__(self, num, nam):
        self.number = num
        self.name = nam

    def printStudData(self):
        print("Number :", self.number)
        print("Name :", self.name)


class ItStudent(Student):
    mar1 = 0
    mar2 = 0
    mar3 = 0
    total = 0
    avg = 0.0

    def __init__(self, num, nam, m1, m2, m3):
        super().__init__(num, nam)
        self.mar1 = m1
        self.mar2 = m2
        self.mar3 = m3

    def calMarks(self):
        self.total = self.mar1 + self.mar2 + self.mar3
        self.avg = self.total / 3

    def printItStudData(self):
        super().printStudData()
        print("Marks 1 :", self.mar1)
        print("Marks 2 :", self.mar2)
        print("Marks 3 :", self.mar3)
        print("Total :", self.total)
        print("Average :", self.avg)


class ManagementStudent(Student):
    viva_date = ""
    final_date = ""

    def __init__(self, num, nam, v_date, f_date):
        super().__init__(num, nam)
        self.viva_date = v_date
        self.final_date = f_date

    def printManStudentData(self):
        super().printStudData()
        print("Viva Date :", self.viva_date)
        print("Final Date :", self.final_date)


#IT Student
num = input("Student Number : ")
name = input("Student Name : ")
m1 = int(input("Mark 1 : "))
m2 = int(input("Mark 2 : "))
m3 = int(input("Mark 3 : "))

obj1 = ItStudent(num, name, m1, m2, m3)

obj1.calMarks()
obj1.printItStudData()


# Management Student
num = input("\nStudent Number : ")
name = input("Student Name : ")
viva = input("Viva Date : ")
final = input("Final Date : ")

obj2 = ManagementStudent(num, name, viva, final)

obj2.printManStudentData()
