"""
Modify the above customer class make set method for each attribute and get met method to return
 and diplay customer destilas.

"""

class Customer:

    # Setter methods
    def setCustname(self, cname):
        self.custname = cname

    def setAccno(self, accno):
        self.accno = accno

    def setAcctype(self, acctype):
        self.acctype = acctype

    def setDepositAmt(self, dep_amt):
        self.deposit_amt = dep_amt
        self.balance = dep_amt

    def setBalance(self, balance):
        self.balance = balance


    # Getter methods
    def getCustname(self):
        return self.custname

    def getAccno(self):
        return self.accno

    def getAcctype(self):
        return self.acctype

    def getDepositAmt(self):
        return self.deposit_amt

    def getBalance(self):
        return self.balance


    # Deposit
    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt


    # Withdrawal
    def withdrawal(self, with_amt):
        if with_amt > self.balance:
            print("Withdraw amount cannot exceed the current balance")
        else:
            self.balance = self.balance - with_amt


    # Display customer details
    def displayBalance(self):
        print("\nCustomer Name :", self.getCustname())
        print("Account Number :", self.getAccno())
        print("Account Type :", self.getAcctype())
        print("Deposit Amount :", self.getDepositAmt())
        print("Current Balance :", self.getBalance())
        print("-----------------------------")


# Create customer object
cust1 = Customer()


# Get customer details
cname = input("Enter customer name: ")
accno = input("Enter account number: ")
acctype = input("Enter account type: ")
d_amt = float(input("Enter initial deposit amount: "))


# Set values using setter methods
cust1.setCustname(cname)
cust1.setAccno(accno)
cust1.setAcctype(acctype)
cust1.setDepositAmt(d_amt)


# Display customer details
print("\nCustomer Registered Successfully!")
cust1.displayBalance()


# Deposit transaction
dep_amt = float(input("\nEnter deposit amount: "))
cust1.deposit(dep_amt)

print("\nAfter Deposit:")
cust1.displayBalance()


# Withdrawal transaction
with_amt = float(input("\nEnter withdrawal amount: "))
cust1.withdrawal(with_amt)

print("\nAfter Withdrawal:")
cust1.displayBalance()

