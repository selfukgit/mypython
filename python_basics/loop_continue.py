#!/usr/bin/python

for letter in 'Python':     # First Example
   if letter == 'h':
      continue #will go to condition,wont execute the following statement
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue #will go to condition, wont execute following statement
   print 'Current variable value :', var
print "Good bye!"
