#Ex 1 : create 3 menu function to take 3 menu function design a simple menu and call each menu  function using a infinit while loop also use the match case structure for calling the menu option 

def mnu1():
    print("Menu 1")


def mnu2():
    print("Menu 2")


def mnu3():
    print("Menu 3")


while True:
    # main program
    print("\nMy menu")
    print("-------")
    print("1. Menu1")
    print("2. Menu2")
    print("3. Menu3")
    print("4. Exit")

    opt = int(input("Enter your option (1/2/3/4): "))

    match opt:
        case 1:
            mnu1()
        case 2:
            mnu2()
        case 3:
            mnu3()
        case 4:
            print("Exiting...")
            break;
