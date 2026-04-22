class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def display(self):   # instance method
        print("Name:", self.name)
        print("Mark:", self.mark)

s = Student("Ram", 90)
s.display()