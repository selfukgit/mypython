class Parent: #define parent class
	parentAttr = 100
	def __init__(self):
		print "calling parent class constructor"
	def parentMethod(self):
		print "calling parent class method"
	def setAttr(self,attr):
		Parent.parentAttr = attr
		self.instanceAttr = attr*10
	def getAttr(self):
		print "Class variable :",Parent.parentAttr,"Instance variable : ",self.instanceAttr
class Child(Parent): #define child class
	def __init__(self):
		print "calling child constructor"
	def childMethod(self):
		print "calling child class menthod"

child = Child()
child.childMethod()
child.parentMethod()
child.setAttr(200)
child.getAttr()

print "checking child class is subclass of parent \n", issubclass(Child,Parent)	
print "checking object child is instance of subclass or parent - same function\n",isinstance(child,Parent)
print "checking object child is instance of subclass or parent - same function\n",isinstance(child,Child)
