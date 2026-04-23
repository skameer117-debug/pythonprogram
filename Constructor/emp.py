class Employee:
	def salary(self):
		print("base salary")
class manager(Employee):
	def salary(self):
		print("manager salary is higher")
m=manager()
m.salary()