from student import *
from subject import *
class GradeBook:
    def __init__(self):
        self.students = {}
        self.subjects = {}
    
    def add_student(self, student_id, student_name):
        if student_id in self.students:
           print(f"Student with ID {student_id} already exists.")
        else:
            self.students[student_id] = Student(student_id, student_name)
            print(f"Student '{student_name}'  has been added successfully.")
    
    def add_subject(self, subject_name, subject_code):
        if subject_name in self.subjects:
            print(f"Subject '{subject_name}' already exists.")
        else:
            self.subjects[subject_name] = Subject(subject_name, subject_code)
            print(f"Subject '{subject_name}' has been added successfully.")
    
    def assign_grade(self, student_id, subject_name, grade):
        student = self.students.get(student_id)
        if student:
            student.add_grade(subject_name,grade)
        else:
            print(f"Student with ID {student_id} not found.")
            
    def get_student_by_id(self, student_id):
        return self.students.get(student_id)
        