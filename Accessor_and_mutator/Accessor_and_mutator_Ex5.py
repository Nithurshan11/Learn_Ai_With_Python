"""
create the class customer and performancr a simple baniking system
include attributes customer name , account , number , accounttype , deposit amount
and curretn balance

Method to do following

1.register a new customer
2.deposit amount
3.withdraw the give amount , after checking the current balance
4.display customer deatils after each bank trncaction

Make one customer object 

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
        print("Customer Name:", self.custname)
        print("Account Number:", self.accno)
        print("Account Type:", self.acctype)
        print("Current Balance:", self.balance)
        print("------------------------")


# Create customer object
cust1 = Customer()

# Register customer
cust1.custReg("Nithurshan", "123456743", "savings", 25000)
cust1.displayBalance()

# Deposit
cust1.deposit(70000)
cust1.displayBalance()

# Withdraw
cust1.withdrawal(150000)
cust1.displayBalance()
