"""
MultiLevel Inherintance

"""

class A:
    x=0;
    def __init__(self, x):
        self.x = x;

    def printDataX(self):
        print("Data X is : " , self.x);

class B(A):

    y="";
    def __init__(self, x,y):
        super().__init__(x);
        self.y=y;

    def printDataY(self):
        super().printDataX();
        print("Data Y is : " , self.y);

class C(B):
    z=0.0;
    def __init__(self, x,y,z):
        super().__init__(x,y)
        self.z = z;

    def printDataZ(self):
        super().printDataY();
        print("Data Z is : " , self.z);

obj1= C(100,"aaa" ,99.9);
obj1.printDataZ();
