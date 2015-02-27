i = 2
while(i < 10):
   j = 2
   print"###################################"
   print "entry loop : i=",i,"j=",j
   while(j <= (i/j)):
      print "In : while loop : j <= (i/j) : j =",j,"i/j=",i/j
      print"i%j",i%j
      print "not(i%j) =",not(i%j)
      if not(i%j): break
      j = j + 1
      print "j=",j
   if (j > i/j) : 
      print "in if : j > i/j,j=",j,",i/j=",i/j
      print i, " is prime"
   i = i + 1
   print"i =",i
   print"####################################"

print "Good bye!"
