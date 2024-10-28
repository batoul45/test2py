class Pupil:
    def __init__(self):
        # Create a dictionary to store students and their subjects
        self.students = {}

    def add_student(self, name, subjects):
        # Add a new student to the dictionary.
        # 'name' is the student's name, and 'subjects' is a single string containing subject names separated by spaces.
        # This splits 'subjects' by spaces to create a list of individual subject names, storing it as the value for that student.
        self.students[name] = subjects.split()

    def show_all(self):
       # Display all students and their subjects, sorted alphabetically by student name in descending order (Z to A).
        # It goes through each student name in sorted order, and prints the name and their list of subjects.
        for name in sorted(self.students.keys(), reverse=True):
            print(f"{name}: {self.students[name]}")

    def student_for_sub(self, student_name):
        # Look up and print the subjects for a given student, if they exist.
        # 'student_name' is the name we’re searching for in the students dictionary.
        # If 'student_name' is found in the dictionary, print their subjects.
        # If not, print a message saying the student was not found.
        if student_name in self.students:
            print(self.students[student_name])
        else:
            print("There are no students with this name.")

    def sub_for_students(self, subject):
        # Find students studying a specific subject
        students_list = [name for name, subjects in self.students.items() if subject in subjects]
        if students_list:
            print(students_list)
        else:
            print("There are no matching students.")


# Creating the Classroom instance
classroom = Pupil()

# Input for students and their subjects
num_students = int(input("Write number of students: "))
for i in range(1, num_students + 1):
    name = input(f"Name of {i} student: ")
    subjects = input(f"Subjects of {i} student: ")
    classroom.add_student(name, subjects)

# Example outputs to test functionality
print("\n>>> show_all()")
Pupil.show_all()

print("\n>>> student_for_sub('Jane')")
classroom.student_for_sub("Jane")

print("\n>>> student_for_sub('Jack')")
classroom.student_for_sub("Jack")

print("\n>>> sub_for_students('math')")
classroom.sub_for_students("math")

print("\n>>> sub_for_students('astronomy')")
classroom.sub_for_students("astronomy")

print("\n>>> sub_for_students('biology')")
classroom.sub_for_students("biology")
