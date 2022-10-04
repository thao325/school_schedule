import pytest
from school_schedule.student import Student

def test_add__new_class():
    # Arrange
    EXPECTED_NAME = "Stacy"
    EXPECTED_GRADE = "Freshman"
    EXPECTED_STARTING_CLASSES = ["English", "Physical"]
    EXPECTED_NEW_CLASS = "Math"
    student1 = Student(EXPECTED_NAME, EXPECTED_GRADE, EXPECTED_STARTING_CLASSES)
    
    # Act
    student1.add_class(EXPECTED_NEW_CLASS)

    # Assert
    assert "English" in student1.classes
    assert "Physical" in student1.classes
    assert EXPECTED_NEW_CLASS in student1.classes
    assert len(student1.classes) == 3

    