"""
using a infinit while loop input index umber and marks for 3 sub and get the toatl , avg and grade and write the input and call details using a txt file using a function
exit the input process in index numbers "0000" finaly read the file and display the student details using another function 
"""


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

    total = mar1 + mar2 + mar3

    avg = total / 3

    if avg >= 50:
        grade = "Pass"
    else:
        grade = "Fail"

    write_stud_data(
        indexno, mar1, mar2, mar3, total, avg, grade
    )


print("Student Performance from the File")
read_stud_data()
