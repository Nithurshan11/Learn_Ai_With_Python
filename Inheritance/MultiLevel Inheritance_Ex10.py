"""
create a class A with a int attrinute , parameter constructure and a print method
make the sub class B with a string attribute sub class constructure derived print method
and methods to write obj B in the file and read the file and display the B data from the
file

"""
class A:
    x = 0

    def __init__(self, xx):
        self.x = xx

    def printDataX(self):
        print("Data X is :", self.x)


class B(A):
    y = ""

    def __init__(self, xx, yy):
        super().__init__(xx)
        self.y = yy

    def printDataY(self):
        super().printDataX()
        print("Data Y is :", self.y)

    def write_Bclass_data(self):
        fp = open("Myfile.txt", "w")
        fp.write(f"Data X : {self.x}\nData Y : {self.y}")
        fp.close()

    def read_Bclass_data(self):
        fp = open("Myfile.txt", "r")

        for file_data in fp:
            print(file_data.strip())

        fp.close()


obj1 = B(100, "aaaa")

obj1.printDataY()
obj1.write_Bclass_data()

print("***** Reading File Data *****")
obj1.read_Bclass_data()
