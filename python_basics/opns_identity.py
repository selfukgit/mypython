a = 20
b = 20
c = (1,2,3)
d = (1,2,3,4)
f = (1,2,3)
# compares the value of it
print "a=",a,"b=",b,"c=",c,"d=",d,"f=",f

if ( c is f ): #gives true in case of a and b but wrong in case of c and f
   print "Line 1 - a and b have same identity"
else:
   print "Line 1 - a and b do not have same identity"

if ( id(c) == id(f) ):
   print "Line 2 - a and b have same identity"
else:
   print "Line 2 - a and b do not have same identity"
print"b = 30"

b = 30
if ( a is b ):
   print "Line 3 - a and b have same identity"
else:
   print "Line 3 - a and b do not have same identity"

if ( a is not b ):
   print "Line 4 - a and b do not have same identity"
else:
   print "Line 4 - a and b have same identity"
