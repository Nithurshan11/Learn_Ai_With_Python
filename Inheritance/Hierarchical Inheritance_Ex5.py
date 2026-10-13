"""
modify the about class input 2 mothods to real the customer details from the text file
and display
"""

class Customer:
    number = ""
    name = ""
    address = ""

    def __init__(self, num, nam, add):
        self.number = num
        self.name = nam
        self.address = add

    def printCustomerData(self):
        print("Customer Number :", self.number)
        print("Customer Name :", self.name)
        print("Address :", self.address)


# Commercial Customer
class CommercialCustomer(Customer):
    units = 0
    total = 0

    def __init__(self, num, nam, add, units):
        super().__init__(num, nam, add)
        self.units = units

    def calBill(self):

        if self.units <= 5:
            self.total = 0

        elif self.units <= 25:
            self.total = (self.units - 5) * 5

        elif self.units <= 50:
            self.total = (20 * 5) + (self.units - 25) * 10

        elif self.units <= 75:
            self.total = (20 * 5) + (25 * 10) + (self.units - 50) * 15

        else:
            self.total = (20 * 5) + (25 * 10) + (25 * 15) + (self.units - 75) * 25

    def printCommercialData(self):
        super().printCustomerData()
        print("Customer Code : C")
        print("Units Consumed :", self.units)
        print("Total Bill : Rs.", self.total)

    def writeFile(self):
        file = open("customers.txt", "a")

        file.write("\nCommercial Customer\n")
        file.write("Customer Number : " + self.number + "\n")
        file.write("Customer Name : " + self.name + "\n")
        file.write("Address : " + self.address + "\n")
        file.write("Units Consumed : " + str(self.units) + "\n")
        file.write("Total Bill : Rs." + str(self.total) + "\n")

        file.close()

    
    def readCommercialFile(self):
        file = open("customers.txt", "r")

        data = file.read()

        print("\n----- Customer File Details -----")
        print(data)

        file.close()


# Domestic Customer
class DomesticCustomer(Customer):
    units = 0
    total = 0

    def __init__(self, num, nam, add, units):
        super().__init__(num, nam, add)
        self.units = units

    def calBill(self):

        if self.units <= 10:
            self.total = 0

        elif self.units <= 25:
            self.total = (self.units - 10) * 3

        elif self.units <= 50:
            self.total = (15 * 3) + (self.units - 25) * 6

        elif self.units <= 75:
            self.total = (15 * 3) + (25 * 6) + (self.units - 50) * 9

        else:
            self.total = (15 * 3) + (25 * 6) + (25 * 9) + (self.units - 75) * 15

    def printDomesticData(self):
        super().printCustomerData()
        print("Customer Code : D")
        print("Units Consumed :", self.units)
        print("Total Bill : Rs.", self.total)

    def writeFile(self):
        file = open("customers.txt", "a")

        file.write("\nDomestic Customer\n")
        file.write("Customer Number : " + self.number + "\n")
        file.write("Customer Name : " + self.name + "\n")
        file.write("Address : " + self.address + "\n")
        file.write("Units Consumed : " + str(self.units) + "\n")
        file.write("Total Bill : Rs." + str(self.total) + "\n")

        file.close()

    def readDomesticFile(self):
        file = open("customers.txt", "r")

        data = file.read()

        print("\n----- Customer File Details -----")
        print(data)

        file.close()



print("----- Commercial Customer -----")

num = input("Customer Number : ")
name = input("Customer Name : ")
address = input("Address : ")
units = int(input("Units Consumed : "))

obj1 = CommercialCustomer(num, name, address, units)

obj1.calBill()

print("\n----- Commercial Customer Details -----")
obj1.printCommercialData()

obj1.writeFile()


print("\n----- Domestic Customer -----")

num = input("Customer Number : ")
name = input("Customer Name : ")
address = input("Address : ")
units = int(input("Units Consumed : "))

obj2 = DomesticCustomer(num, name, address, units)

obj2.calBill()

print("\n----- Domestic Customer Details -----")
obj2.printDomesticData()

obj2.writeFile()


print("\n===== Reading Details From File =====")

obj1.readCommercialFile()
