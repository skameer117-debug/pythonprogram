class Student:
	def __init__(self,r,n,m):
		self.r=r
		self.nm=n
		self.mark=m
	def show(self):
		print("my name=",self.nm)
		print("rollno=",self.r)
		print("mark=",self.mark)
s=Student(1,"ram",90.50)
s.show()