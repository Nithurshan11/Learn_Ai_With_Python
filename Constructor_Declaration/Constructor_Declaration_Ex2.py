"""
Create a Python class called Parts with the following attributes:

Part name
Code number
Manufacturing date
Cost

Use a parameterized constructor (__init__) to initialize these attributes.

Create getter methods to return each attribute.

Finally, create one object of the Parts class and display all the part details using the getter methods

"""
class Parts:
    pname = ""
    pnum = ""
    pdate = ""
    cost = 0.0

    def __init__(self, pname, pnum, pdate, cost):
        self.pname = pname
        self.pnum = pnum
        self.pdate = pdate
        self.cost = cost

    def getName(self):
        return self.pname

    def getNumber(self):
        return self.pnum

    def getManu(self):
        return self.pdate

    def getCost(self):
        return self.cost


obj1 = Parts("Hard Disk", "0121", "11/12/2000", 20000)

print("Parts Name:", obj1.getName())
print("Parts Number:", obj1.getNumber())
print("Parts Manufacture:", obj1.getManu())
print("Cost:", obj1.getCost())

    
    

























    

