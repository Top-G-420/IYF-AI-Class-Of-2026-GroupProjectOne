from your_script_name import remove_student # Replace 'your_script_name' with your actual filename

def test_remove_student_success():
    # Setup a mock list
    students = [{"name": "John Doe", "grade": "A"}]
    # Call the function with the list and a name
    remove_student(students, "John Doe")
    # Check if the list is now empty
    assert len(students) == 0

def test_remove_student_not_found():
    students = [{"name": "John Doe"}]
    remove_student(students, "Jane Smith")
    # List should still have 1 student
    assert len(students) == 1
