"""
Make the product class with attribyte (product code no , name , and manufactured company )
make setters and getters foe each attribute create one product object

"""

class product:
    s_id="";
    s_name="";
    s_manu="";

    def setid(self , s_id):
        self.s_id = s_id;

    def setName(self , s_name):
        self.s_name = s_name;

    def setManu(self , s_manu):
        self.s_manu = s_manu;


    def getid(self):
        return self.s_id;

    def getName(self):
        return self.s_name;
    
    def getManu(self):
        return self.s_manu;



myprod = product();

myprod.setid("0001");
myprod.setName("HardWare");
myprod.setManu("aaa");


#Print the modified value
print("Id :" , myprod.getid());
print("Name :" , myprod.getName());
print("Manufacture :" , myprod.getManu());









