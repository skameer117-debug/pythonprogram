class student:
	def __init__(self,r,n,m1,m2,m3):
		self.r=r
		self.nm=n
		self.m1=m1
		self.m2=m2
		self.m3=m3
	def show(self):
		print("my name=",self.nm)
		print("my rollno=",self.r)
		print("my mark1=",self.m1)
		print("my mark2=",self.m2)
		print("my mark3=",self.m3)
		t=self.total()
		print("total mark=",t)
		print("avg mark=",t/3)
	def total(self):
		return self.m1+self.m2+self.m3
s=student(1,"ram",90,80,70)
s.show()