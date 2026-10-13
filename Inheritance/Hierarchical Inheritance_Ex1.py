"""
Hierarchical Inheritance

        A
       / \
      B   C
"""

class A:
    x = 0

    def __init__(self, xx):
        self.x = xx

    def printDataX(self):
        print("Data X is :", self.x)


class B(A):
    y = 0.0

    def __init__(self, xx, yy):
        super().__init__(xx)
        self.y = yy

    def printDataY(self):
        super().printDataX()
        print("Data Y is :", self.y)


class C(A):
    z = ""

    def __init__(self, xx, zz):
        super().__init__(xx)
        self.z = zz

    def printDataZ(self):
        super().printDataX()
        print("Data Z is :", self.z)


obj1 = B(100, 10.5)

print("Object of class B - information")
obj1.printDataY()


obj2 = C(200, "Python")

print("Object of class C - information")
obj2.printDataZ()
