class JustCounter:
	__secretCount = 0 #hidden member(Data hiding)
	def count(self):
		self.__secretCount += 1
		print self.__secretCount
		#print JustCounter.__secretCount #only prints the initial value of __secretCount .... not object specific value 

counter = JustCounter()
counter.count()
counter.count()

print counter._JustCounter__secretCount #permissible format : object._classname__attrName
print counter.__secretCount #gives error 
