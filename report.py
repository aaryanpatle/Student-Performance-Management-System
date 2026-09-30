from calculator import findtotal
from calculator import find_percentage
from grade import find_grade


def show_report(student):

    marks = student["marks"]

    total = findtotal(marks)
    percentage = find_percentage(marks)
    grade = find_grade(percentage)

    print("       STUDENT REPORT")

    print("RollNumber :", student["rollno"])
    print("Name        :", student["name"])

    print("\nMarks:")

    for i in range(len(marks)):
        print("Subject", i + 1, ":", marks[i])

    print("\nTotal       :", total)
    print("Percentage  :", round(percentage, 2), "%")
    print("Grade       :", grade)

    print("-----------------------------")