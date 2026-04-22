class employee:
	def __init__(self,a,n,m):
		self.a=a
		self.nm=n
		self.salary=m
	def show(self):
		print("my name=",self.nm)
		print("age=",self.a)
		print("salary=",self.salary)
s=employee(26,"ram",6000)
s.show()
s1=employee(30,"sam",7000)
s1.show()
s2=employee(35,"hari",10000)
s2.show()
s3=employee(65,"karan",60000)
s3.show()
s4=employee(70,"krish",65000)
s4.show()