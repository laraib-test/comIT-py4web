"""
SCHOOL MANAGEMENT SYSTEM - STUDENT TEMPLATE
===========================================
Instructions: Fill in the missing code in the methods marked with TODO.
Follow the comments to complete each class.
"""

# ============================================
# STEP 1: STUDENT CLASS
# ============================================

class Student:
    """
    TODO: Create a class to represent a student.
    
    Instructions:
    1. Create the __init__ method with parameters: self, student_id, name, grade_level
    2. Store these as instance variables
    3. Create a display_info method that prints student details
    4. Create __str__ method for string representation
    """
    
    def __init__(self, student_id, name, grade_level):
        # TODO: Initialize the attributes
        # YOUR CODE HERE
        self.student_id = student_id
        self.name = name
        self.grade_level = grade_level
        
    
def display_info(self):
        # TODO: Print student information in a formatted way
        # Example: "ID: 1001 | Name: Alice | Grade: 10"
        # YOUR CODE HERE
        print(f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade_level}")
        pass
    
def __str__(self):
        # TODO: Return a string representation of the student
        # Example: "Student(ID: 1001, Name: Alice, Grade: 10)"
        # YOUR CODE HERE
        return f"Student(ID: {self.student_id}, Name: {self.name}, Grade: {self.grade_level})"


# ============================================
# STEP 2: CLASS CLASS (School Course)
# ============================================

class Class:
    """
    TODO: Create a class to represent a school course.
    
    Instructions:
    1. Initialize with class_id, class_name, teacher
    2. Create an empty list for enrolled_students
    3. Create methods to add/remove students
    4. Create method to list all students in the class
    """
    
    def __init__(self, class_id, class_name, teacher):
        # TODO: Initialize attributes and an empty list for enrolled students
        # YOUR CODE HERE
        self.class_id = class_id
        self.class_name = class_name
        self.teacher = teacher
        self.enrolled_students = []
        pass
    
    def add_student(self, student):
        # TODO: Add a student to the enrolled_students list
        # Check if student is already enrolled to avoid duplicates
        # Print success or warning message
        # YOUR CODE HERE
            if student not in self.enrolled_students:
             self.enrolled_students.append(student)
             print(f"Success: {student.name} has been enrolled in {self.class_name}.")
            else:
             print(f"Warning: {student.name} is already enrolled in {self.class_name}.")

            
    
    def remove_student(self, student):
        # TODO: Remove a student from the enrolled_students list
        # Check if student exists before removing
        # Print appropriate messages
        # YOUR CODE HERE
     if student in self.enrolled_students:
         self.enrolled_students.remove(student)
         print(f"{student.name} has been removed from {self.class_name}.")
     else:
        print(f"{student.name} is not enrolled in {self.class_name}.")
        pass
    
    def list_students(self):
        # TODO: Display all students enrolled in this class
        # Handle case when no students are enrolled
        # YOUR CODE HERE
        print(f"Class: {self.class_name} | Teacher: {self.teacher}")
        if not self.enrolled_students:
         print(f"No students are currently enrolled in {self.class_name}.")
        else:
         for student in self.enrolled_students:
          print(f"- {student.name} (ID: {student.student_id})")
        pass
    
    def __str__(self):
        # TODO: Return string representation of the class
        # Include class ID, name, teacher, and number of students
        # YOUR CODE HERE
        return f"Class(ID: {self.class_id}, Name: {self.class_name}, Teacher: {self.teacher}, Students: {len(self.enrolled_students)})"


# ============================================
# STEP 3: GRADE CLASS
# ============================================

class Grade:
    """
    TODO: Create a class to represent a student's grade in a class.
    
    Instructions:
    1. Initialize with grade_id, student, class_obj, score
    2. Create a method to convert numerical score to letter grade
    3. Create a method to display grade information
    """
    
    def __init__(self, grade_id, student, class_obj, score):
        # TODO: Initialize all attributes
        # YOUR CODE HERE
        self.grade_id = grade_id
        self.student = student
        self.class_obj = class_obj
        self.score = score
        
    
    def get_letter_grade(self):
        """
        Convert numerical score to letter grade.
        Use this scale:
        90-100: A
        80-89: B
        70-79: C
        60-69: D
        Below 60: F
        """
        # TODO: Return the appropriate letter grade based on self.score
        # YOUR CODE HERE
        if self.score >= 90: return "A"
        elif self.score >= 80: return "B"
        elif self.score >= 70: return "C"
        elif self.score >= 60: return "D"
        else:  return "F"
        
    
    def display_grade(self):
        # TODO: Print grade information including letter grade
        # Example: "Grade ID: 301 | Student: Alice | Class: Math | Score: 95 | Letter: A"
        # YOUR CODE HERE
        letter = self.get_letter_grade()
        print(f"Grade ID: {self.grade_id} | Student: {self.student.name} | Class: {self.class_obj.class_name} | Score: {self.score} | Letter: {letter}")
        
    
    def __str__(self):
        # TODO: Return string representation of the grade
        # Include letter grade in the string
        # YOUR CODE HERE
        letter = self.get_letter_grade()
        return f"Grade(ID: {self.grade_id}, Student: {self.student.name}, Class: {self.class_obj.class_name}, Score: {self.score}, Letter: {letter})"
        


# ============================================
# STEP 4: SCHOOL MANAGEMENT SYSTEM
# ============================================

class School:
    """
    TODO: Create the main school management class.
    
    This class will manage all students, classes, and grades.
    """
    
    def __init__(self, school_name):
        # TODO: Initialize school name and empty lists for students, classes, and grades
        # YOUR CODE HERE
        self.school_name = school_name
        self.students = []
        self.classes = []
        self.grades = []
        
    
    # ---------- STUDENT MANAGEMENT ----------
    
    def add_student(self, student_id, name, grade_level):
        # TODO: Create a new Student object and add to students list
        # Check if student_id already exists
        # Return the new student or None if failed
        # YOUR CODE HERE
            for student in self.students:
                if student.student_id == student_id:
                    print(f"Warning: Student ID {student_id} already exists.")
                    return None  # Student already exists
                new_student = Student(student_id, name, grade_level)
                self.students.append(new_student)
                return new_student

    def find_student(self, student_id):
        # TODO: Find and return a student by ID
        # Return None if not found
        # YOUR CODE HERE
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def list_all_students(self):
        # TODO: Display all students in the school
        # Handle empty list case
        # YOUR CODE HERE
        print(f"Students in {self.school_name}:")
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(student)
        
    
    # ---------- CLASS MANAGEMENT ----------
    
    def add_class(self, class_id, class_name, teacher):
        # TODO: Create a new Class object and add to classes list
        # Check if class_id already exists
        # Return the new class or None if failed
        # YOUR CODE HERE
        for class_obj in self.classes:
            if class_obj.class_id == class_id:
                print(f"Warning: Class ID {class_id} already exists.")
                return None  # Class already exists
        new_class = Class(class_id, class_name, teacher)
        self.classes.append(new_class)
        return new_class

    def find_class(self, class_id):
        # TODO: Find and return a class by ID
        # Return None if not found
        # YOUR CODE HERE
        for class_obj in self.classes:
            if class_obj.class_id == class_id:
                return class_obj
        return None

    def list_all_classes(self):
        # TODO: Display all classes in the school
        # Include number of students enrolled in each class
        # YOUR CODE HERE
        print(f"Classes in {self.school_name}:")
        for class_obj in self.classes:
            print(f"ID: {class_obj.class_id} | Name: {class_obj.class_name} | Enrolled Students: {len(class_obj.enrolled_students)}")
    # ---------- ENROLLMENT MANAGEMENT ----------
    
    def enroll_student_in_class(self, student_id, class_id):
        # TODO: Enroll a student in a class
        # Find both student and class first
        # Use the class's add_student method
        # Return True if successful, False otherwise
        # YOUR CODE HERE
        student = self.find_student(student_id)
        course =self.find_class(class_id)
        if student and course:
            course.add_student(student)
            return True
        return False

    # ---------- GRADE MANAGEMENT ----------
    
    def add_grade(self, grade_id, student_id, class_id, score):
        # TODO: Add a grade for a student in a class
        # Verify student and class exist
        # Verify student is enrolled in the class
        # Check if grade_id already exists
        # Create and add new Grade object
        # YOUR CODE HERE
        student = self.find_student(student_id)
        course = self.find_class(class_id)
        if student and course and (student in course.enrolled_students):
            # Check if grade_id already exists

            new_grade = Grade(grade_id, student, course, score)
            self.grades.append(new_grade)
            return True
        return False

    def list_grades_for_student(self, student_id):
        # TODO: Display all grades for a specific student
        # YOUR CODE HERE
        student = self.find_student(student_id)
        if student:
            print(f"Grades for {student.name}:")
            for grade in self.grades:
                if grade.student == student:
                    print(f" - {grade.class_obj.class_name}: {grade.score}")
        else:
            print("Student not found.")

    def list_grades_for_class(self, class_id):
        # TODO: Display all grades for a specific class
        # YOUR CODE HERE
        class_obj = self.find_class(class_id)
        if class_obj:
            print(f"Grades for {class_obj.class_name}:")
            for grade in self.grades:
                if grade.class_obj == class_obj:
                    print(f" - {grade.student.name}: {grade.score}")
        else:
            print("Class not found.")

    def calculate_student_average(self, student_id):
        # TODO: Calculate and display average grade for a student
        # Return the average or None if no grades
        # YOUR CODE HERE
        student = self.find_student(student_id)
        if student:
            total_score = sum(grade.score for grade in self.grades if grade.student == student)
            num_grades = sum(1 for grade in self.grades if grade.student == student)
            if num_grades > 0:
                average = total_score / num_grades
                print(f"Average grade for {student.name}: {average:.2f}")
                return average
        print("Student not found or no grades available.")
        return None


# ============================================
# STEP 5: MAIN PROGRAM WITH SAMPLE DATA
# ============================================

def main():
    """
    TODO: Create the main program with sample data and menu system.
    
    Instructions:
    1. Create a School object
    2. Add sample data (students, classes, enrollments, grades)
    3. Create an interactive menu system
    """
    
    print("=" * 60)
    print("🏫 WELCOME TO THE SCHOOL MANAGEMENT SYSTEM 🏫")
    print("=" * 60)
    
    # TODO: Create your school
    school = School("ABC High School")
    
    # TODO: Add sample students
    # Use the data from the tutorial or create your own
    student1 = school.add_student(1001, "Alice", 10)
    student2 = school.add_student(1002, "Bob", 11)
    student3 = school.add_student(1003, "Charlie", 12)
    
    # TODO: Add sample classes
    class1 = school.add_class(2001, "Mathematics", "Mr. Smith")
    class2 = school.add_class(2002, "Science", "Ms. Johnson")
    class3 = school.add_class(2003, "History", "Mr. Williams")
    
    # TODO: Enroll students in classes
    school.enroll_student_in_class(1001, 2001)  # Alice in Math
    school.enroll_student_in_class(1001, 2002)  # Alice in Science
    school.enroll_student_in_class(1002, 2001)  # Bob in Math
    school.enroll_student_in_class(1003, 2003)  # Charlie in History
    
    # TODO: Add sample grades
    school.add_grade(3001, 1001, 2001, 85)  # Alice's Math grade
    school.add_grade(3002, 1001, 2002, 90)  # Alice's Science grade
    school.add_grade(3003, 1002, 2001, 78)  # Bob's Math grade
    school.add_grade(3004, 1003, 2003, 88)  # Charlie's History grade
    
    # TODO: Create the interactive menu system
    # Include options to:
    # - List all students
    # - List all classes
    # - Add a new student
    # - Add a new class
    # - Enroll student in class
    # - Add a grade
    # - View student grades
    # - View class grades
    # - Calculate student average
    # - Exit
    
    # HINT: Use a while loop and if/elif statements for the menu
    
    # YOUR CODE HERE
    while True:
        print("\n--- MENU ---")
        print("1. List all students")
        print("2. List all classes")
        print("3. Add a new student")
        print("4. Add a new class")
        print("5. Enroll student in class")
        print("6. Add a grade")
        print("7. View student grades")
        print("8. View class grades")
        print("9. Calculate student average")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            school.find_student()
            student_id = int(input("Enter student ID: "))
            student = school.find_student(student_id)
            if student:
                print(student)
            else:
                print("Student not found.")
            
        elif choice == "2":
            school.list_all_classes()
        elif choice == "3":
            # TODO: Implement add student functionality
            student_id = int(input("Enter student ID: "))
            student_name = input("Enter student name: ")
            student_grade = int(input("Enter student grade: "))
            school.add_student(student_id, student_name, student_grade)
        elif choice == "4":
            # TODO: Implement add class functionality
            class_id = int(input("Enter class ID: "))
            class_name = input("Enter class name: ")
            teacher_name = input("Enter teacher name: ")
            school.add_class(class_id, class_name, teacher_name)
        elif choice == "5":
            # TODO: Implement enroll student in class functionality
            student_id = int(input("Enter student ID: "))
            class_id = int(input("Enter class ID: "))
            school.enroll_student_in_class(student_id, class_id)
        elif choice == "6":
            # TODO: Implement add grade functionality
            grade_id = int(input("Enter grade ID: "))
            student_id = int(input("Enter student ID: "))
            class_id = int(input("Enter class ID: "))
            grade = int(input("Enter grade: "))
            school.add_grade(grade_id, student_id, class_id, grade)
        elif choice == "7":
            # TODO: Implement view student grades functionality
            student_id = int(input("Enter student ID: "))
            school.view_student_grades(student_id)
        elif choice == "8":
            # TODO: Implement view class grades functionality
            class_id = int(input("Enter class ID: "))
            school.view_class_grades(class_id)
        elif choice == "9":
            # TODO: Implement calculate student average functionality
            student_id = int(input("Enter student ID: "))
            school.calculate_student_average(student_id)
        elif choice == "10":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
 main()


# ============================================
# BONUS CHALLENGES (Optional)
# ============================================

"""
Once you complete the basic system, try these challenges:

1. Add a Teacher class with attributes (teacher_id, name, subjects)
2. Add a method to calculate class average
3. Add search functionality (find students by name)
4. Add data persistence (save to and load from a file)
5. Add a report card generator
6. Add GPA calculation (4.0 scale)
7. Add attendance tracking
8. Add student schedules/timetables
"""

# ============================================
# ANSWER KEY (For teachers)
# ============================================

"""
The complete solution is available in the tutorial document.
Students should refer to the tutorial for guidance but try to
write the code themselves first.
"""

