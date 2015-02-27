a = 20
b = 20
c = (1,2,3)
d = (1,2,3,4)
e = (1,2,3)
f = [1,2,3]
g = [1,2,3]

h = "str"
i = "str"
print "#######################################################"
print "a=",a
print "b=",b
print "c =",c
print "d =",d
print "e =",e
if ( a is b ): #gives true in case of a and b but wrong in case of c and f
   print a," and",b,"have same identity"
else:
   print a," and",b,"have different identity"
if ( c is e ): #gives true in case of a and b but wrong in case of c and f
   print c," and",e,"have same identity"
else:
   print c," and",e,"have different identity"
if ( f is not g ): #gives true in case of a and b but wrong in case of c and f
   print f," and",g,"have different identity"
else:
   print f," and",g,"have same identity"
if ( h is not i ): #gives true in case of a and b but wrong in case of c and f
   print h," and",i,"have different identity"
else:
   print h," and",i,"have same identity"
