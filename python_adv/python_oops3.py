class Parent:
	def parentMethod(self):
		print "parent method"
class Child:
	def parentMethod(self): #overridden method of parent menthod
		print "calling overridden method of parentMethod()"

c = Child()
c.parentMethod()
