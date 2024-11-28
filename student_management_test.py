import unittest
from student_management import StudentManagement, Student


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        self.system = StudentManagement()
        
        

    def test_add_student(self):
        self.system.students = []  
        self.system.add_student(1, "John Doe", 20, "VG", ["Math", "Science"]) 
        self.assertEqual(len(self.system.students), 1)  

    def test_view_students(self):
        result = self.system.view_students() 
        self.assertIn("John Doe", result) 

    def test_update_student(self):
        self.system.update_student(1,"Updated Name")  
        self.assertEqual(self.system.students[0].name, "Updated Name") 

    def test_delete_student(self):
        self.system.add_student(2, "John Doe", 20, "VG", ["Math", "Science"])
        self.system.delete_student(2) 
        self.assertEqual(len(self.system.students), 1)  

    def test_save_students_to_file(self):       
        self.system.save_students_to_file()
        with open("student.txt", "r") as file:
            data = file.read()
        self.assertIn('"name": "John Doe"', data)

    def test_load_students_from_file(self):
        with open("student.txt", "w") as file:
            file.write(
                '[{"id": 1, "name": "John Doe", "age": 18, "grade": "VG", "subjects": ["Math", "Science"]}]'
            )
        self.system.load_students_from_file()
        self.assertEqual(self.system.students[0].name, "John Doe")
if __name__ == "__main__":
    unittest.main()
