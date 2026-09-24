"""
Create a Python class called Customer with the following attributes:

Customer Number
Customer Name
Customer Code
Units Consumed
Total Bill Amount

Use a parameterized constructor to initialize Customer Number, Name, Code, and Units Consumed.

Create a setter method to calculate the total bill amount using the following conditions:

Commercial Customer — Code C

Units 1–5 → Free
Units 6–25 → Rs. 5 per unit
Units 26–50 → Rs. 10 per unit
Units 51–75 → Rs. 15 per unit
Above 75 → Rs. 25 per unit

Domestic Customer — Code D

Units 1–10 → Free
Units 11–25 → Rs. 5 per unit
Units 26–50 → Rs. 3 per unit
Units 51–75 → Rs. 6 per unit
Above 75 → Rs. 9 per unit

Create getter methods to return each attribute.

The program should accept multiple customers until the user enters 000 as the customer number. Calculate and display each customer's bill and save the customer details into a file called Customer.txt.
"""

class Customer:

    def __init__(self, num, name, code, unit):
        self.num = num
        self.name = name
        self.code = code
        self.unit = unit
        self.billanum = 0.0

    # Setter method to calculate bill
    def setBillanum(self):

        # Commercial Customer
        if self.code == "C" or self.code == "c":

            if self.unit > 75:
                self.billanum = ((self.unit - 75) * 25) + \
                                ((75 - 50) * 15) + \
                                ((50 - 25) * 10) + \
                                ((25 - 5) * 5)

            elif self.unit > 50:
                self.billanum = ((self.unit - 50) * 15) + \
                                ((50 - 25) * 10) + \
                                ((25 - 5) * 5)

            elif self.unit > 25:
                self.billanum = ((self.unit - 25) * 10) + \
                                ((25 - 5) * 5)

            elif self.unit > 5:
                self.billanum = (self.unit - 5) * 5

            else:
                self.billanum = 0

        # Domestic Customer
        elif self.code == "D" or self.code == "d":

            if self.unit > 75:
                self.billanum = ((self.unit - 75) * 9) + \
                                ((75 - 50) * 6) + \
                                ((50 - 25) * 3) + \
                                ((25 - 10) * 5)

            elif self.unit > 50:
                self.billanum = ((self.unit - 50) * 6) + \
                                ((50 - 25) * 3) + \
                                ((25 - 10) * 5)

            elif self.unit > 25:
                self.billanum = ((self.unit - 25) * 3) + \
                                ((25 - 10) * 5)

            elif self.unit > 10:
                self.billanum = (self.unit - 10) * 5

            else:
                self.billanum = 0

    # Getter methods
    def getNumber(self):
        return self.num

    def getName(self):
        return self.name

    def getCode(self):
        return self.code

    def getUnits(self):
        return self.unit

    def getBillanum(self):
        return self.billanum

    # Write data to file
    def writeFile(self):

        fp = open("Customer.txt", "a")

        fp.write(
            f"Customer Number : {self.num}\n"
            f"Customer Name : {self.name}\n"
            f"Customer Code : {self.code}\n"
            f"Units Consumed : {self.unit}\n"
            f"Total Bill Amount : {self.billanum}\n\n"
        )

        fp.close()


# Main Program
while True:

    num = input("Enter Customer Number : ")

    if num == "000":
        break

    name = input("Enter Customer Name : ")
    code = input("Enter Customer Code (C/D) : ")
    unit = int(input("Enter Units Consumed : "))

    # Create object
    obj1 = Customer(num, name, code, unit)

    # Calculate bill
    obj1.setBillanum()

    # Save to file
    obj1.writeFile()

    # Display customer details
    print("\nCustomer Number :", obj1.getNumber())
    print("Customer Name :", obj1.getName())
    print("Customer Code :", obj1.getCode())
    print("Units Consumed :", obj1.getUnits())
    print("Total Bill Amount :", obj1.getBillanum())
    print()