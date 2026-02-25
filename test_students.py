from remove_student import remove_student

def test_remove_student_logic(monkeypatch):
    # 1. Create a sample list to test with
    test_list = [{"name": "Alice Smith", "age": 20, "marks": 90}]
    
    # 2. Simulate the user typing "Alice Smith"
    monkeypatch.setattr('builtins.input', lambda _: "Alice Smith")
    
    # 3. Run your function
    remove_student(test_list)
    
    # 4. If the student was removed, the list should be empty
    assert len(test_list) == 0

def test_remove_student_not_found(monkeypatch):
    test_list = [{"name": "Alice Smith"}]
    # Simulate typing a name that is NOT in the list
    monkeypatch.setattr('builtins.input', lambda _: "Bob Brown")
    
    remove_student(test_list)
    
    # The list should still have 1 student
    assert len(test_list) == 1
