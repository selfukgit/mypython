#!/usr/bin/python
limit_lower = int(raw_input("Enter lower number limit\n"))
limit_higher = int(raw_input("Enter upper limit\n"))

for num in range(limit_lower,limit_higher):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'
