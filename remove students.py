def remove_student(students, name):
    target = " ".join(name.split()).title()
    for student in students:
        if student["name"] == target:
            students.remove(student)
            print("Student removed successfully!")
            return 
    print("Student not found")
