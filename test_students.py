from remove_student import remove_student

def test_remove_student_logic(monkeypatch):
    # Create a test list with one student dictionary
    test_list = [{"name": "Alice Smith", "age": 20, "marks": 90}]
    
    # Simulate user typing "Alice Smith"
    monkeypatch.setattr('builtins.input', lambda _: "Alice Smith")
    
    # Run the function
    remove_student(test_list)
    
    # If the student was removed, the list should be empty (length 0)
    assert len(test_list) == 0

def test_remove_student_not_found(monkeypatch):
    test_list = [{"name": "Alice Smith"}]
    
    # Simulate typing a name that is NOT in the list
    monkeypatch.setattr('builtins.input', lambda _: "Bob Brown")
    
    remove_student(test_list)
    
    # The list should still have the 1 original student
    assert len(test_list) == 1
