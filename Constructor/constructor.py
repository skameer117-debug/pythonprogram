class person:
	def __init__(self,name):
		self.name=name
		print("person constructor called")
class Student(person):
	def __init__(self, name):
		super().__init__(name)
		print("Student constructor called")
s=Student("Rohit")