fp1 = open("emp.txt", "a")


def emp_salary_cal(number, name, salary):

    if salary > 200000:
        allo = salary * 0.20
        bonus = salary * 0.10

    elif salary > 100000:
        allo = salary * 0.10
        bonus = salary * 0.05

    else:
        allo = salary * 0.05
        bonus = salary * 0.025

    g_salary = salary + allo + bonus

    fp1.write(
        f"Employee Number : {number}\n"
        f"Employee Name : {name}\n"
        f"Basic Salary : {salary}\n"
        f"Allowance : {allo}\n"
        f"Bonus : {bonus}\n"
        f"Gross Salary : {g_salary}\n\n"
    )


while True:

    number = input("Enter Employee Number: ")

    if number == "000":
        break

    name = input("Enter Employee Name: ")
    salary = float(input("Enter Basic Salary: "))

    emp_salary_cal(number, name, salary)


fp1.close()

print("Employee records saved successfully.")












