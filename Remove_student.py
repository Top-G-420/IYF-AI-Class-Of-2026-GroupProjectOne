def remove_student(students):
    raw_name = input("What is the students name to remove? ").strip()
    rem_student = " ".join(raw_name.split()).title()
    
    for student in students:
        if student["name"] == rem_student:
            students.remove(student)
            print("Student removed successfully!")
            return 
            
    print("Student not found")
