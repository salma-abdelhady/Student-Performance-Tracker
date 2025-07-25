"""Add students
  * Add subjects
  * Assign grades
  * Calculate GPAs
  * View full reports
  * Overrides display_dashboard()
"""
  
from user import *
from student import *
from subject import *

class Admin(User):
    def __init__(self,username, gradebook):
      super().__init__(username, Admin)
      self.gradebook = gradebook
    
    def display_dashboard(self):
      print(f"\n ===== Admin Dashboard ({self.username}) =====")
      print("1) Add student")
      print("2) Add subject")
      print("3) Assign grade")
      print("4) Calculate GPA")
      print("5) Print all students")
      print("6) View student report")
      print("7) Exit")
      
    def add_student(self, student_id, name):
      self.gradebook.add_student(student_id, name)

    def add_subject(self, subject_name):
      self.gradebook.add_subject(subject_name)

    def assign_grade(self, student_id, subject, grade):
      self.gradebook.assign_grade(student_id, subject, grade)

    def calculate_gpa(self, student_id):
      student = self.gradebook.get_student_by_id(student_id)
      if student:
        gpa = student.calculate_gpa()
        print(f"GPA for student {student.get_name()} (ID: {student_id}): {gpa:.2f}")
      else:
        print(f"Student with ID {student_id} not found.")

    def view_full_report(self):
      if not self.gradebook.students:
        print("No students in the system. ")
        return
      
      print("\n===== All Student Reports =====")
      for student in self.gradebook.students.values():
        student.get_report()
        print("-" * 40)