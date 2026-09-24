"""
Accessor and mutator

Make the student class eith id and name as attributes create accessor and mutator method for both attribut to
input and return id and name make one obj

"""

#Defining class student
class student:
    s_id="";
    s_name="";

    #Defining Mutator Method
    def setid(self , s_id):
        self.s_id = s_id;

    #Defining Mutator Method
    def setName(seld , s_name):
        seld.s_name = s_name;

    #Defining Accessor Mehtod
    def getid(self):
        return self.s_id;

    def getName(self):
        return self.s_name;


#Creating an object
mystud = student();

#Modifiying the value of the variable
#using mutator method

mystud.setid("005");
mystud.setName("Mala");

#Print the modified value
print("Id " , mystud.getid());
print("Id " , mystud.getName());








