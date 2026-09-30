import io
import contextlib
import unittest

from student import Student
from report import show_report


class StudentSystemTests(unittest.TestCase):
    def test_student_details_use_rollno_key(self):
        student = Student("101", "Alice", [80, 90, 85])
        self.assertEqual(student.get_details()["rollno"], "101")

    def test_report_uses_rollno_key(self):
        student = {"rollno": "101", "name": "Alice", "marks": [80, 90, 85]}

        with contextlib.redirect_stdout(io.StringIO()) as stdout:
            show_report(student)

        output = stdout.getvalue()
        self.assertIn("RollNumber :", output)
        self.assertIn("101", output)


if __name__ == "__main__":
    unittest.main()
