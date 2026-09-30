from student import Student
from database import add_student
from database import load_students
from database import find_student
from report import show_report


def add_new_student():

    print("\n New Student ")

    rollno = input("roll number: ")
    name = input(" student name: ")

    marks = []

    print("\n marks out of 100:")

    for i in range(5):

        while True:

            try:
                mark = float(input(" marks for Subject " + str(i + 1) + ": "))

                if mark >= 0 and mark <= 100:
                    marks.append(mark)
                    break

                else:
                    print(" marks between 0 and 100.")

            except ValueError:
                print("Please enter a number.")

    student = Student(rollno, name, marks)

    add_student(student)

    print("\nStudent added successfully")


def display_all_students():

    students = load_students()

    if len(students) == 0:
        print("\nThere are no students")
        return

    for student in students:
        show_report(student)


def search_student():

    roll_no = input("\n roll number to search: ")

    student = find_student(roll_no)

    if student is not None:
        show_report(student)

    else:
        print("\n not found.")


def main():

    while True:

       
        print("  STUDENT PERFORMANCE SYSTEM")
       

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("\nEnter your choice ")

        if choice == "1":
            add_new_student()

        elif choice == "2":
            display_all_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("\nThank you")
            break

        else:
            print("\nenter a valid choice.")


if __name__ == "__main__":
    main()