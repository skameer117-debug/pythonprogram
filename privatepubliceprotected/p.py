class Student:
	def __init__(self):
		self.__marks=90
	def __show(self):
		print("private method")
	def acess_private(self):
		print(self.__marks)
		self.__show()
s=Student()
s.acess_private()