"""

input emp id name and salary using a function find the designamction

designaction is manager or staff basic salary over 1 million are manager others saff write all
manager and staff deatils in text file "Manager.txt" and "staff.txt" respectively perfoem this for 5 emp

"""

fp1 = open("Manager.txt", "a")
fp2 = open("Staff.txt", "a")


def emp_data(empno, name, salary):

    if salary > 1000000:
        designation = "Manager"

        fp1.write(
            f"Employee Number : {empno}\n"
            f"Name : {name}\n"
            f"Designation : {designation}\n"
            f"Salary : {salary}\n\n"
        )

    else:
        designation = "Staff"

        fp2.write(
            f"Employee Number : {empno}\n"
            f"Name : {name}\n"
            f"Designation : {designation}\n"
            f"Salary : {salary}\n\n"
        )


# Collect data for 5 employees
x = 1

while x <= 5:

    empno = input("Enter Employee Number: ")
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Basic Salary: "))

    emp_data(empno, name, salary)

    x += 1


fp1.close()
fp2.close()

print("Employee records saved successfully.")

























