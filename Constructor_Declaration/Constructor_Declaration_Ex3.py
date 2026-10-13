"""

Create  the student class with attribute

name
marks for 3 sub
total and avg
use parametes constructure and inilixe student object with name and 3 marks
set method to call total and avg . get method to return each attribute , ma
Make one student object
"""

class Student:
    name = ""
    mark1 = 0
    mark2 = 0
    mark3 = 0
    total = 0
    avg = 0.0

    # Parameterized constructor
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    # Set total
    def setTotal(self):
        self.total = self.mark1 + self.mark2 + self.mark3

    # Set average
    def setAverage(self):
        self.avg = self.total / 3

    # Getter methods
    def getName(self):
        return self.name

    def getMark1(self):
        return self.mark1

    def getMark2(self):
        return self.mark2

    def getMark3(self):
        return self.mark3

    def getTotal(self):
        return self.total

    def getAverage(self):
        return self.avg


# Create student object
obj1 = Student("Nidurshan", 80, 75, 90)

# Call setter methods
obj1.setTotal()
obj1.setAverage()

# Display details
print("Student Name:", obj1.getName())
print("Total:", obj1.getTotal())
print("Average:", obj1.getAverage())
