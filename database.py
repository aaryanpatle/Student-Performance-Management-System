import json

file_name = "students.json"


def load_students():

    try:
        with open(file_name, "r") as file:
            students = json.load(file)

        return students

    except FileNotFoundError:
        return []


def save_students(students):

    with open(file_name, "w") as file:
        json.dump(students, file, indent=4)


def add_student(student):

    students = load_students()

    students.append(student.get_details())

    save_students(students)


def find_student(roll_no):

    students = load_students()

    for student in students:

        if student["rollno"] == roll_no:
            return student

    return None