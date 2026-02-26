def remove_student(students, name):
    # Format the name (handles spaces and caps)
    target = " ".join(name.split()).title()
    
    # Simple search and remove
    for student in students:
        if student["name"] == target:
            students.remove(student)
            print("Student removed successfully!")
            return  # Stop once we find them
            
    print("Student not found")
