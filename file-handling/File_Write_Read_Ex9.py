"""

Modify the above program to write the performance detailes into two sepertate text file
"pass.txt" and "fail.txt" assume avg above 75 are pass other are fail stud .

2/ reade both file and display pass and fail student
3/ use seperate function to write pass and fail student

"""


def cal(m1, m2, m3):
    total = m1 + m2 + m3
    avg = total / 3

    if avg >= 75:
        grade = "pass"
    else:
        grade = "fail"

    return total, avg, grade


def write_pass_student(no, m1, m2, m3, total, avg, grade):

    fp = open("pass.txt", "a")

    fp.write(
        f"Index Number : {no}\n"
        f"Marks 1 : {m1}\n"
        f"Marks 2 : {m2}\n"
        f"Marks 3 : {m3}\n"
        f"Total: {total}\n"
        f"Average : {avg:.2f}\n"
        f"Grade : {grade}\n"
        f"\n"
    )

    fp.close()

def write_fail_student(no, m1, m2, m3, total, avg, grade):

    fp = open("fail.txt", "a")

    fp.write(
        f"Index Number : {no}\n"
        f"Marks 1 : {m1}\n"
        f"Marks 2 : {m2}\n"
        f"Marks 3 : {m3}\n"
        f"Total : {total}\n"
        f"Average: {avg:.2f}\n"
        f"Grade : {grade}\n"
        f"\n"
    )

    fp.close()


def read_pass_students():

    fp = open("pass.txt", "r")
    
    for stud_rec in fp:
        print(stud_rec.strip())

    fp.close()


def read_fail_students():

    fp = open("fail.txt", "r")

    for stud_rec in fp:
        print(stud_rec.strip())

    fp.close()


while True:

    indexno = input("Enter the index number : ")

    if indexno == "0000":
        break

    mar1 = int(input("Enter Marks 1 : "))
    mar2 = int(input("Enter Marks 2 : "))
    mar3 = int(input("Enter Marks 3 : "))

    total, avg, grade = cal(mar1, mar2, mar3)

    if grade == "pass":

        write_pass_student(indexno,mar1,mar2,mar3,total,avg,grade )

    else:

        write_fail_student(indexno, mar1, mar2, mar3, total,avg,grade)


print("\nStudent Performance from Files")

read_pass_students()
read_fail_students()














        
