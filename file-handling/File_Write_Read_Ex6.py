
"""
Use an infinfit loop to collect emo id, name and salary . exit the input when id is  "0000"
use function to do following

1 . cal gross salary , by adding 10% binus for salary over 100000 otherwise 5% bonus salary
below 100000

2. write the salary details in the file

3 read the file and dipslay the details

"""

def write_Emp_Data(id, name, salary, gross_salary):
    fp = open("Emp2.txt", "a")

    fp.write(
        f"Employee ID : {id}\n"
        f"Employee Name : {name}\n"
        f"Salary : {salary}\n"
        f"Gross Salary : {gross_salary}\n"
        f"----------------------\n"
    )

    fp.close()


def read_Emp_Data():
    fp = open("Emp2.txt", "r")

    for emp_rec in fp:
        print(emp_rec.strip())

    fp.close()


while True:

    id_no = input("Enter Employee ID number : ")

    if id_no == "0000":
        break

    name = input("Enter Employee Name : ")
    salary = float(input("Enter Employee Salary : "))

    if salary > 100000:
        gross_salary = salary + (salary * 0.10)
    else:
        gross_salary = salary + (salary * 0.05)

    write_Emp_Data(id_no, name, salary, gross_salary)


print("Employee Salary Details...")
read_Emp_Data()
