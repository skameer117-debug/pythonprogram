class Student:
    def __init__(self, name, mark):
        self.name = name      # instance variable
        self.mark = mark

s1 = Student("Ram", 90)
s2 = Student("Shyam", 80)

print(s1.name, s1.mark)
print(s2.name, s2.mark)