
def remove_student(students):
    # Ask for input and clean up the formatting
    raw_name = input("What is the students name to remove? ").strip()
    rem_student = " ".join(raw_name.split()).title()
    
    # Loop through the list to find the match
    for student in students:
        if student["name"] == rem_student:
            students.remove(student)
            print("Student removed successfully!")
            return 
            
    print("Student not found")
