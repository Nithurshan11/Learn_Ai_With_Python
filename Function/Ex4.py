"""
create a function to do following

1.create following menu structure

   My Menu
 ----------
 1.Input Emp details
 2.cal Gross Salary
 3.Display Emp Deatils
 4.Exit

 Enter a option(1/2/3/4):

2. Input Emp Name and Salary

3. Cal gross Salary with the below condition
   
   basic_salary >100000
     add bonus 25% from the basic salary
   basic_salary <=100000
     add bonus 10% from the basic salary
  
4.Display all the EMp details

"""


def print_menu():
    print("My Menu")
    print("--------")
    print("1. Input Employee Details: ")
    print("2.calculate Gross Salary: ")
    print("3. Display()")
    print("4. Exit()")

emp_name=""
salary=0
gross_sal=0


def inp():

    global emp_name , salary
    emp_name=(input("Enter Youe Name: "))
    salary=float(input("Enter your Salart: "))

def cal():

    global gross_sal

    if salary>100000:
    
        gross_sal=salary +(salary * 0.25)
    
    else:
        gross_sal=salary + (salary * 0.10)
    

def display():

    print("Employe Name: ", emp_name)
    print("Employee Salary: ", salary)
    print("Gross Salary: ", gross_sal)

while True:

    print_menu()
    opt=int(input(" Enter a option(1/2/3/4): "))

    match opt:
        case 1:
            inp()
        case 2:
            cal()
        case 3:
            display()
        case 4:
            print("Exit the Menu")
            break
        case _:
            print("Invalied option..")
        
