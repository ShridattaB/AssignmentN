

class School():
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = School("shr", 2)
s2 = School("aditya", 5)
s3 = School("anil", 10)

students = [s1, s2, s3]
for student in students:
    print(f"Name: {student.name}, Roll: {student.roll}")
