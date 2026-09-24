"""
Modify the main program get real time input to register the customer
custname , accno , acctype and deposti amount and deposti and withdreaw trancaction each

"""

class Customer:
    def custReg(self, cname, accno, acctype, d_amt):
        self.custname = cname
        self.accno = accno
        self.acctype = acctype
        self.deposit_amt = d_amt
        self.balance = d_amt

    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt

    def withdrawal(self, with_amt):
        if with_amt > self.balance:
            print("Withdraw amount cannot exceed the current balance")
        else:
            self.balance = self.balance - with_amt

    def displayBalance(self):
        print("\nCustomer Name :", self.custname)
        print("Account Number :", self.accno)
        print("Account Type :", self.acctype)
        print("Current Balance :", self.balance)
        print("-----------------------------")


# Create customer object
cust1 = Customer()

# Get customer details
cname = input("Enter customer name: ")
accno = input("Enter account number: ")
acctype = input("Enter account type: ")
d_amt = float(input("Enter initial deposit amount: "))

# Register customer
cust1.custReg(cname, accno, acctype, d_amt)

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

