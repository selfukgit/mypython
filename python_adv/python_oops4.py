class Vector:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def __str__(self):
		return "Vector(%d,%d)"%(self.a,self.b)
	def __add__(self,other):
		return Vector(self.a + other.a,self.b + other.b)

v1 = Vector(2,1)
v2 = Vector(8,9)

print v1 + v2 #goes to add function and then str function to print : __add__ ----> __str__
