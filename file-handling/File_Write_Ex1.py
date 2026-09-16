"""
open a text file
get the input of 3 students
1.index number and marks for 2 subject using a function stud_data()
2.cal the toatl and avg
3.display both cal

write the student recode in text file "Stud1"

"""

fp = open("Stud1.txt", "a")


def stud_data(number, mar1, mar2):
    total = mar1 + mar2
    avg = total / 2

    print("Total Marks:", total)
    print("Average Marks:", avg)

    fp.write(
        f"Number: {number}\n"
        f"Marks 1: {mar1}\n"
        f"Marks 2: {mar2}\n"
        f"Total Marks: {total}\n"
        f"Average Marks: {avg}\n"
        f"------------------\n"
    )


x = 1

while x <= 3:
    number = input("Enter Index Number: ")
    mar1 = int(input("Enter Marks 1: "))
    mar2 = int(input("Enter Marks 2: "))

    stud_data(number, mar1, mar2)

    x += 1

fp.close()
