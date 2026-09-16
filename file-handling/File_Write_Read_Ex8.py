"""

modify the previous program make function to do following

1. call toatl avg and select the grade
2 . write and read the student deatails to the txt file
"""


def cal(m1, m2, m3):
    global total, average, grade

    total = m1 + m2 + m3
    average = total / 3

    if average > 50:
        grade = "Pass"
    else:
        grade = "Fail"


def write_stud_data(no, m1, m2, m3, tot, avg, grd):
    fp = open("Stud2.txt", "a")

    fp.write(
        f"Index Number : {no}\n"
        f"Marks 1 : {m1}\n"
        f"Marks 2 : {m2}\n"
        f"Marks 3 : {m3}\n"
        f"Total Marks : {tot}\n"
        f"Average Marks : {avg}\n"
        f"Grade : {grd}\n"
        f"\n"
    )

    fp.close()


def read_stud_data():
    fp = open("Stud2.txt", "r")

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

    cal(mar1, mar2, mar3)

    write_stud_data(
        indexno,
        mar1,
        mar2,
        mar3,
        total,
        average,
        grade
    )


print("Student Performance from the File")
read_stud_data()
