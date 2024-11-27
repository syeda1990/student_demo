import json

class Student:
    def __init__(self, student_id, name, age, grade, subjects):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects

    def update_student_info(self, name=None, age=None, grade=None, subjects=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if grade:
            self.grade = grade
        if subjects:
            self.subjects = subjects

    def display_student(self):
        return f"""
        ID: {self.student_id}
        Name: {self.name}
        Age: {self.age}
        Grade: {self.grade}
        Subjects: {', '.join(self.subjects)}
        """

class StudentManagement:
    def __init__(self):
        self.students = []
        self.load_students_from_file()

    def add_student(self, student_id, name, age, grade, subjects):
        id_exists = False
        for student in self.students:
            if student.student_id == student_id:
                id_exists = True  
                break
        if id_exists:
            print("ID already exists. Please enter a unique ID.")
            return "ID already exists."
        self.students.append(Student(student_id, name, age, grade, subjects))
        return "Student added successfully."

    def view_students(self):
        if not self.students:
            return "No students found."
        return "\n".join(student.display_student() for student in self.students)
        
    
    def update_student(self, student_id, name=None, age=None, grade=None, subjects=None):
        #student = next((s for s in self.students if s.student_id == student_id), None)
        student = None
        for s in self.students:
            if s.student_id == student_id:
                student = s  
                break 
        if not student:
            return "Student not found."
        student.update_student_info(name, age, grade, subjects)
        return "Student information updated successfully."

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return "Student deleted successfully."
        return "Student not found."

    def save_students_to_file(self):
        try:
            with open("student.txt", "w") as file:
                student_data = [] 
                for student in self.students:
                    student_info = {
                        "id": student.student_id,
                        "name": student.name,
                        "age": student.age,
                        "grade": student.grade,
                        "subjects": student.subjects
                    }
                    student_data.append(student_info)
                file.write(json.dumps(student_data, indent=4))
            return "Students saved to file."
        except IOError:
            return "Error saving to file."

    def load_students_from_file(self):
        try:
            with open("student.txt", "r") as file:
                student_data = json.load(file)
                for student_info in student_data:
                    student = Student(
                        student_id=student_info["id"],
                        name=student_info["name"],
                        age=student_info["age"],
                        grade=student_info["grade"],
                        subjects=student_info["subjects"]
                    )
                    self.students.append(student)
        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist.
        except IOError:
            return "Error reading file."
        

        

if __name__ == "__main__":

    system = StudentManagement()
    

    while True:
        print("\n--- Student Management System ---")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Update a student information")
        print("4. Remove a student information")
        print("5. Save to a File and Exit")
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                student_id = int(input("Enter Student ID: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                grade = input("Enter Grade: ")
                subjects = input("Enter Subjects (comma-separated): ").split(',')
                print(system.add_student(student_id, name, age, grade, [s.strip() for s in subjects]))
            elif choice == 2:
                print(system.view_students())
            elif choice == 3:
                student_id = int(input("Enter Student ID to update: "))
                name = input("Enter new Name (or leave blank): ") or None
                age = input("Enter new Age (or leave blank): ") 
                grade = input("Enter new Grade (or leave blank): ") or None
                subjects = input("Enter new Subjects (comma-separated, or leave blank): ")
                age = int(age) if age.isdigit() else None
                subjects = [s.strip() for s in subjects.split(',')] if subjects else None
                print(system.update_student(student_id, name, age, grade, subjects))
            elif choice == 4:
                student_id = int(input("Enter Student ID to delete: "))
                print(system.delete_student(student_id))
            elif choice == 5:
                print(system.save_students_to_file())
                break
            else:
                print("Invalid choice. Please select again.")
        except ValueError:
            print("Invalid input. Please try again.")
