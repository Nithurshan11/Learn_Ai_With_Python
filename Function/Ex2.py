
#peform a simple calculator program by including all arictmatic operaction for 2 int inputes use match case for operactor selection
        
num1= int(input("Enter a Integer 1 :"));
oper= input("Enter Arithmetic Operaction [+ - * / // %] :");
num2 = int(input("Enter Integer 2 :"));


match oper:
    case "+":
        result = num1+num2;
    case "-":
        result = num1-num2;
    case "*":
        result = num1*num2;
    case "/":
        result = num1/num2;
    case "//":
        result = num1//num2;
    case "%":
        result = num1%num2;
    case _:
        result ="invalied operaction";

print("Result is " , num1 , " " , oper ," " , num2 , " = ", result);
        
        
        
