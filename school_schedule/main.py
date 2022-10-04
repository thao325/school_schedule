from school_schedule.high_school_student import HighSchoolStudent

# First instance
claire = HighSchoolStudent(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ],
                has_parking_privileges=True,
                clubs=["Algorithms Club"]
            )
#Second instance
quinn= HighSchoolStudent(
                "Quinn", 
                "sophmore", 
                [
                    "Geometry", 
                    "Writing II", 
                    "Computer Science", 
                    "Gym", 
                    "Life Science", 
                    "Band"
                ],
                has_parking_privileges=True,
                clubs=["Drama Club"]
            )
students = [quinn, claire]
for student in students:
    print(student.summary())
