"""
Create a Python class called Customer with the following attributes:

Customer Number
Customer Name
Customer Code
Units Consumed
Total Bill Amount

Use a parameterized constructor to initialize the customer number, name, code, and units consumed.

Create a setter method to calculate the total bill amount according to the following conditions:

Commercial Customer – Code C

Units	Rate
1–5	Free
6–25	Rs. 5 per unit
26–50	Rs. 10 per unit
51–75	Rs. 15 per unit
Above 75	Rs. 25 per unit

Domestic Customer – Code D

Units	Rate
1–10	Free
11–25	Rs. 5 per unit
26–50	Rs. 3 per unit
51–75	Rs. 6 per unit
Above 75	Rs. 9 per unit

Create getter methods to return each attribute.

Create a writeFile() method to save each customer's details into a text file called Customer.txt.

Use an infinite while loop to enter customer details continuously. When the customer number is 000, terminate the loop.

For every customer:

Create a Customer object.
Calculate the bill amount.
Write the customer details to Customer.txt.
Display the customer details on the screen.
"""


class Customer:
    num = ""
    name = ""
    code = ""
    unit = 0
    billanum = 0.0

    # Parameterized constructor
    def __init__(self, num, name, code, unit):
        self.num = num
        self.name = name
        self.code = code
        self.unit = unit
        self.billanum = 0.0

    # Write customer details to file
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

    # Setter to calculate bill amount
    def setBillanum(self):

        # Commercial
        if (self.code == 'C') or (self.code == 'c'):

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

        # Domestic
        elif (self.code == 'D') or (self.code == 'd'):

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


# Infinite loop
while True:

    num = input("Enter Customer Number (000 to exit): ")

    if num == "000":
        break

    name = input("Enter Customer Name: ")
    code = input("Enter Customer Code (C/D): ")
    unit = int(input("Enter Customer Unit: "))

    # Create object
    obj1 = Customer(num, name, code, unit)

    # Calculate bill
    obj1.setBillanum()

    # Write to file
    obj1.writeFile()

    # Display details
    print("\nCustomer Number:", obj1.getNumber())
    print("Customer Name:", obj1.getName())
    print("Customer Code:", obj1.getCode())
    print("Units Consumed:", obj1.getUnits())
    print("Total Bill Amount:", obj1.getBillanum())
    print()


print("All customer records saved successfully.")
