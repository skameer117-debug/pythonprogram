class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_school(cls):   # class method
        print("School:", cls.school)

Student.show_school()