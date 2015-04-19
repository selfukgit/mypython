#Python classes and objects
class Employee:
	"Common base class for employees"
	empCount = 0
	#constructor of the class Employee
	def __init__(self,name,salary):#self is being called by python itself
		self.name = name
		self.salary = salary
		Employee.empCount += 1
	def displayCount(self):
		print "Total number of employees = %d" %Employee.empCount
	def displayEmployee(self):
		print "Name : ",self.name,",Salary : ",self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
emp1.displayCount()
#adding attributes
emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
emp2.height = 6.3
del emp1.age  # Delete 'age' attribute.
print "Employee 2 height : ",emp2.height

#checking the attributes 
print "check emp1 has attribute age or not : ",hasattr(emp1,'age')
print "getting attribute value of height : ",getattr(emp2,"height")
print "setting attribute of number to emp1 :",setattr(emp1,"num",23123)
print "getting attribute val of num for emp1 : ",getattr(emp1,"num")
print "delete attribute num :",delattr(emp1,"num")
print "\nbuilt in class attributes\n"
print "Employee.__doc__:\n", Employee.__doc__
print "Employee.__name__:\n", Employee.__name__
print "Employee.__module__:\n", Employee.__module__
print "Employee.__bases__:\n", Employee.__bases__
print "Employee.__dict__:\n", Employee.__dict__
