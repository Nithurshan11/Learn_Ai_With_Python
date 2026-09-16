"""
Collect 5 student index numbers and average marks.
Write passed students to pass.txt and failed students to fail.txt.
"""

fp1 = open("pass.txt", "a")
fp2 = open("fail.txt", "a")

def stud_data(indexno, name, avg):

    if avg >= 75:
        grade = "PASS"
        fp1.write(
            f"Index Number : {indexno}\n"
            f"Name : {name}\n"
            f"Average : {avg}\n"
            f"Grade : {grade}\n\n"
        )
    else:
        grade = "FAIL"
        fp2.write(
            f"Index Number : {indexno}\n"
            f"Name : {name}\n"
            f"Average : {avg}\n"
            f"Grade : {grade}\n\n"
        )

# Collect data for 5 students
x = 1
while x <= 5:
    index_number = input("Enter Student Index Number: ")
    name = input("Enter Student Name: ")
    avg = float(input("Enter Average Marks: "))

    stud_data(index_number, name, avg)

    x += 1

fp1.close()
fp2.close()

print("Student records saved successfully.")




