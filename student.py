class Student:

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def get_details(self):
        student = {
            "rollno": self.roll_no,
            "name": self.name,
            "marks": self.marks
        }

        return student