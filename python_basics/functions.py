print "###############variable length arguments ##########################"

def printvariable(*vartuple):
	"This function prints a variable number of arguments"
	#print arg1
	for var in vartuple:
		print var
		#return
#if there is no return then we can leave return stmt	

#calling printvariable
printvariable()
printvariable(10)
printvariable(10,-2,3,4,567)

print " function called by default arguments #############################"
# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )
print "###########function called by keyword arguments ##############"
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print "Name: ", name;
   print "Age ", age;
   return;

# Now you can call printinfo function
printinfo( age='Name', name=67 );#just reversed and checked
print "##########################pass by val/ref######################"
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist
print "############################pass by reference and val ##############"
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist
print "##################################################"
def printstr(str) :
	"this prints a passed string into the function"
	print str
	return 

#function call
printstr("I am the first call to the function printstr\n")
printstr("I am the second call to the function printstr")

