def view_students(students):
    if not students:
        print("No students found.")
    else:
        for i, student in enumerate(students, start=1):
            name, age, marks = student
            print(f"{i}. Name: {name}, Age: {age}, Marks: {marks}")
            