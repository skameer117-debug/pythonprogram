from abc import ABC ,abstractmethod
class shape(ABC):
	@abstractmethod
	def area(self):
		pass
class circle(shape):
	def area(self):
		print("area of circle")
class rectangle(shape):
	def area(self):
		print("area of rectangle")
c=circle()
c.area()
r=rectangle()
r.area()