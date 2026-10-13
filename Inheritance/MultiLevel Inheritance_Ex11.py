"""
modifi the above program by including 2 additional methods for the sub class
ItStudent to read and write the student deatils in the text file

"""

class Student:

    id = ""
    name = ""

    def __init__(self, s_id, s_name):
        self.id = s_id
        self.name = s_name

    def printStudData(self):
        print("Id : ", self.id)
        print("Name : ", self.name)


class SWStudent(Student):

    duration = ""
    fees = 0.0

    def __init__(self, s_id, s_name, dur, fee):
        super().__init__(s_id, s_name)
        self.duration = dur
        self.fees = fee

    def printSWStudData(self):
        super().printStudData()
        print("Duration : ", self.duration)
        print("Fees : ", self.fees)


class ITStudent(SWStudent):

    mar1 = 0
    mar2 = 0
    mar3 = 0
    total = 0
    average = 0.0

    def __init__(self, s_id, s_name, dur, fee, m1, m2, m3):
        super().__init__(s_id, s_name, dur, fee)
        self.mar1 = m1
        self.mar2 = m2
        self.mar3 = m3

    def calMarks(self):
        self.total = self.mar1 + self.mar2 + self.mar3
        self.average = self.total / 3

    def printITStudData(self):
        super().printSWStudData()
        print("Marks 1 : ", self.mar1)
        print("Marks 2 : ", self.mar2)
        print("Marks 3 : ", self.mar3)
        print("Total Marks : ", self.total)
        print("Average Marks : ", self.average)

    def writeFile(self):
        fp = open("Student.txt", "w")

        fp.write(f"ID : {self.id}\n")
        fp.write(f"Name : {self.name}\n")
        fp.write(f"Duration : {self.duration}\n")
        fp.write(f"Fees : {self.fees}\n")
        fp.write(f"Mark 1 : {self.mar1}\n")
        fp.write(f"Mark 2 : {self.mar2}\n")
        fp.write(f"Mark 3 : {self.mar3}\n")
        fp.write(f"Total : {self.total}\n")
        fp.write(f"Average : {self.average}\n")

        fp.close()

    
    def readFile(self):
        fp = open("Student.txt", "r")

        for data in fp:
            print(data.strip())

        fp.close()


obj1 = ITStudent("1234", "Davin", "2 Years",
                 250000.00, 74, 84, 97)

obj1.calMarks()
obj1.printITStudData()

obj1.writeFile()

print("\n***** Reading File Data *****")
obj1.readFile()
