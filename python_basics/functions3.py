print " ###################global vs. local ###########################"
total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print "Inside the function local total : ", total
   return total;

# Now you can call sum function
sum( 10, 20 );
print "Outside the function global total : ", total 
print "#################### return stmt - real example manipulated #######################"
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print "Inside the function : ", total
   return total;

# Now you can call sum function
total1 = 90 + sum( 10, 20 );
print "Outside the function : ", total1 

print "##############lambda --- anonimous functions###################"
#function definision is here
sum = lambda arg1,arg2 : arg1+arg2 #lambda requires and expression always

#now we can call sum as a function

print "Value of total : ", sum( 10,20)
print "Value of total : ", sum( 20,344444)
