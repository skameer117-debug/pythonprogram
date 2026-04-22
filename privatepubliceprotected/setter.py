class Student:
	def __init__(self):
		self.__marks=0
	def get_marks(self):
		return self.__marks
	def set_marks(self,m):
		if m>=0 and m<=100:
			self._marks = m
		else:
			print("Invalid Marks")
s = Student()
s.set_marks(85)
print(s.get_marks())
s.set_marks(150)