from gradebook import *
from admin import *

def main():
    gradebook = GradeBook()
    admin = Admin("admin", gradebook)
    
    while True:
        admin.display_dashboard()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            admin.add_student(student_id, name)
            
        elif choice == "2":
            subject_name = input("Enter Subject Name: ")
            subject_code = input("Enter Subject Code: ")
            admin.add_subject(subject_name, subject_code)
            
        elif choice == "3":
            student_id = input("Enter Student ID: ")
            subject_name = input("Enter Subject: ")
            grade = float(input("Enter Grade: "))
            admin.assign_grade(student_id, subject_name, grade)
            
        elif choice == "4":
            student_id = input("Enter Student ID: ")
            admin.calculate_gpa(student_id)
            
        elif choice == "5":
            admin.view_full_report()
            
        elif choice == "6":
            student_id = input("Enter Student ID: ")
            student = gradebook.get_student_by_id(student_id)
            if student:
                student.get_report()
            else:
                print("Student not found.")
                
        elif choice == "7":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")
            
if __name__ == "__main__":
    main()