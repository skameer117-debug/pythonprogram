class Student:
	def __init__(self, name, marks):
		self.name=name
		self.marks=marks
	def __str__(self):
		return f"name:{self.name},marks:{self.marks}"
s=Student("Rohit",90)
print(s)