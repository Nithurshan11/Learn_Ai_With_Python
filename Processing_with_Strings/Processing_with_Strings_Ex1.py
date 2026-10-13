"""
Inheritance

Single Inheritance
-------------------

Class A

x =0;
def __init__()
def printDataX()

class B

y = ""
def __init__()
def printDataY()
"""

class A:
    x=0;
    def __init__(self , xx):
        self.x = xx;

    def printDataX(self):
        print("Data X is :" , self.x);

class B(A):
    y = "";
    def __init__(self,xx , yy):
        super().__init__(xx);
        self.y = yy;

    def printDataY(self):
        super().printDataX();
        print("Data Y is :" , self.y);

obj1 = B(100 , "aaa");
obj1.printDataY();
        
