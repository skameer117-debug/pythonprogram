class Student:
	def __init__(self, marks):
		self.marks=marks
	def __add__(self, other):
		return self.marks + other.marks
s1=Student(50)
s2=Student(60)
print(s1+s2)