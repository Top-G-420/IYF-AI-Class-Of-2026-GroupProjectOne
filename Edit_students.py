def edit_student(students, search_name):
    for student in students:
        if student["name"] == search_name:
            student["age"] = int(input("Enter new age: "))
            student["marks"] = int(input("Enter new marks: "))
            print("Student updated:", student)
            return
    print("Student not found.")
