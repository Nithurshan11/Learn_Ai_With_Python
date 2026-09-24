"""

Create the emp class with attribute (emp no , name, salary , bonus and gross
salary)input them and call bonus and gross salary add 25% bonus from basic salary
return the input and call and display them

"""
class Employee:
    s_id = ""
    s_name = ""
    s_salary = 0.0
    s_bonus = 0.0
    s_gross = 0.0

    def setid(self, s_id):
        self.s_id = s_id

    def setName(self, s_name):
        self.s_name = s_name

    def setSalary(self, s_salary):
        self.s_salary = s_salary

    def setBonus(self):
        self.s_bonus = self.s_salary * 0.25

    def setGross(self):
        self.s_gross = self.s_salary + self.s_bonus

    def getid(self):
        return self.s_id

    def getName(self):
        return self.s_name

    def getsalary(self):
        return self.s_salary

    def getbonus(self):
        return self.s_bonus

    def getgross(self):
        return self.s_gross


myemp = Employee()

myemp.setid("0001")
myemp.setName("HardWare")
myemp.setSalary(120000.00)
myemp.setBonus()
myemp.setGross()


# Print the values
print("Id :", myemp.getid())
print("Name :", myemp.getName())
print("Salary :", myemp.getsalary())
print("Bonus Salary :", myemp.getbonus())
print("Gross Salary :", myemp.getgross())









