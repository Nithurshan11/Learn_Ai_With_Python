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
            self.total = (15 * 3) + (25 * 6) + \
                         (self.units - 50) * 9

        else:
            self.total = (15 * 3) + (25 * 6) + \
                         (25 * 9) + (self.units - 75) * 15


    def printDomesticData(self):

        super().printCustomerData()

        print("Customer Type : Domestic")
        print("Units Consumed :", self.units)
        print("Total Bill : Rs.", self.total)


    def writeFile(self):

        file = open("customers.txt", "a")

        file.write("Customer Number : " + self.number + "\n")
        file.write("Customer Name : " + self.name + "\n")
        file.write("Address : " + self.address + "\n")
        file.write("Customer Type : Domestic\n")
        file.write("Units Consumed : " + str(self.units) + "\n")
        file.write("Total Bill : Rs." + str(self.total) + "\n")
        file.write("-----------------------------\n")

        file.close()


    def readFile(self, searchNumber):

        file = open("customers.txt", "r")

        customers = file.read().split("-----------------------------")

        found = False

        for customer in customers:

            if ("Customer Number : " + searchNumber) in customer:

               
                print("       CUSTOMER FOUND")

                print(customer.strip())


                found = True
                break

        if found == False:
            print("\nCustomer Not Found!")

        file.close()


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
            self.total = (20 * 5) + \
                         (self.units - 25) * 10

        elif self.units <= 75:
            self.total = (20 * 5) + \
                         (25 * 10) + \
                         (self.units - 50) * 15

        else:
            self.total = (20 * 5) + \
                         (25 * 10) + \
                         (25 * 15) + \
                         (self.units - 75) * 25


    def printCommercialData(self):

        super().printCustomerData()

        print("Customer Type : Commercial")
        print("Units Consumed :", self.units)
        print("Total Bill : Rs.", self.total)


    def writeFile(self):

        file = open("customers.txt", "a")

        file.write("Customer Number : " + self.number + "\n")
        file.write("Customer Name : " + self.name + "\n")
        file.write("Address : " + self.address + "\n")
        file.write("Customer Type : Commercial\n")
        file.write("Units Consumed : " + str(self.units) + "\n")
        file.write("Total Bill : Rs." + str(self.total) + "\n")
        file.write("-----------------------------\n")

        file.close()


    def readFile(self, searchNumber):

        file = open("customers.txt", "r")

        customers = file.read().split("-----------------------------")

        found = False

        for customer in customers:

            if ("Customer Number : " + searchNumber) in customer:

                print("CUSTOMER FOUND")

                print(customer.strip())


                found = True
                break

        if found == False:
            print("\nCustomer Not Found!")

        file.close()

while True:

    code = input(
        "Enter Domestic(D/d), Commercial(C/c), XXX - Stop : "
    )


   
    if code.upper() == "XXX":

        print("Program Stopped")
        break


    elif code.upper() == "D":

        print("\n--- Domestic Customer ---")

        num = input("Customer Number : ")
        name = input("Customer Name : ")
        address = input("Address : ")
        units = int(input("Units Consumed : "))


        obj1 = DomesticCustomer(
            num,
            name,
            address,
            units
        )


        obj1.calBill()


        print("\n--- Customer Bill ---")

        obj1.printDomesticData()


        obj1.writeFile()


        choice = input(
            "\nDo you want to read customer details? (Y/N) : "
        )


        if choice.upper() == "Y":

            searchNum = input(
                "Enter Customer Number : "
            )

            obj1.readFile(searchNum)



    elif code.upper() == "C":

        print("\n--- Commercial Customer ---")

        num = input("Customer Number : ")
        name = input("Customer Name : ")
        address = input("Address : ")
        units = int(input("Units Consumed : "))


        obj2 = CommercialCustomer(
            num,
            name,
            address,
            units
        )


        obj2.calBill()


        print("\n--- Customer Bill ---")

        obj2.printCommercialData()


        obj2.writeFile()


        choice = input(
            "\nDo you want to read customer details? (Y/N) : "
        )


        if choice.upper() == "Y":

            searchNum = input(
                "Enter Customer Number : "
            )

            obj2.readFile(searchNum)



    else:

        print("\nInvalid Input!")
