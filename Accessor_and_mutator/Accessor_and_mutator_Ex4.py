"""
Make the student class with name , 3 marks , total ,avg for attribute
set method to input name and 3 marks and call total and avg , get to return each data
"""
class Student:
    s_name = "";
    s_m1 = 0;
    s_m2 = 0;
    s_m3 = 0;
    s_tot = 0;
    s_avg = 0.0;

    def setName(self, s_name):
        self.s_name = s_name

    def setmarks1(self, s_m1):
        self.s_m1 = s_m1

    def setmarks2(self, s_m2):
        self.s_m2 = s_m2

    def setmarks3(self, s_m3):
        self.s_m3 = s_m3

    def setTotal(self):
        self.s_tot = self.s_m1 + self.s_m2 + self.s_m3

    def setAverage(self):
        self.s_avg = self.s_tot / 3

    def getName(self):
        return self.s_name

    def getm1(self):
        return self.s_m1

    def getm2(self):
        return self.s_m2

    def getm3(self):
        return self.s_m3

    def gettotal(self):
        return self.s_tot

    def getaverage(self):
        return self.s_avg


mystu = Student()

mystu.setName("Kala")
mystu.setmarks1(90)
mystu.setmarks2(80)
mystu.setmarks3(70)

mystu.setTotal()
mystu.setAverage()


# Print the values
print("Name :", mystu.getName())
print("Marks 1 :", mystu.getm1())
print("Marks 2 :", mystu.getm2())
print("Marks 3 :", mystu.getm3())
print("Total :", mystu.gettotal())
print("Average :", mystu.getaverage())
