class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name

print(Student.school)