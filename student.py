class Student:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__grades = {}
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def add_grade(self, subject, grade):
        if subject not in self.__grades:
            if grade >= 0 and grade <= 100:
                self.__grades[subject] = grade 
            else:
                raise ValueError("Grade must be between 0 and 100.")
        else:
            print(f"Grade for '{subject}' already exists.")
            
    def calculate_gpa(self):
        if not self.__grades:
            return 0.0
        
        return sum(self.__grades.values()) / len(self.__grades)    
    
    def get_report(self):
        print(f"Student Id: {self.__id}, Student name: {self.__name}")
        print("Student Grades: ")
        for subject,grade in self.__grades.items():
            print(f"{subject} : {grade}")
        
        print(f"GPA: {self.calculate_gpa():.2f}")
    
    