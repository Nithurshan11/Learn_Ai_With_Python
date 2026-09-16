#create the function to do followings 
#1) calling the menu structure 
#2)input 3 num 
#3)get the total , avg cal
#4) display both cal
#5)using an infinit while loop get a input and call the function for the process


def menu_print():
    print("My Menu")
    print("--------")
    print("1. Input()")
    print("2.calculate()")
    print("3. Display()")
    print("4. Exit()")

def inp():
    global num1 , num2 , num3; #The global keyword lets you change a variable outside a function.
    num1=int(input("Enter Integer 1: "))
    num2=int(input("Enter Integer 2: "))
    num3=int(input("Enter Integer 3: "))

def cal():
    global tot , avg
    tot = num1 + num2 + num3
    avg= tot/3

def disp():
    print("Total: ",  tot)
    print("Average: ", avg)

while True:
    menu_print()
    opt= int(input("Enter your option(1/2/3/4): "))

    match opt:
        case 1:
            inp()
        case 2:
            cal()
        case 3:
            disp()
        case 4:
            print("Exit the menu")
            break
        case _:
            print("Invalied option..")
        
            
