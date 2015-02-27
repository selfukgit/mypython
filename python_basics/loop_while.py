var = 1
while var >0 :
   var = var + 1 
   if var <3 :
        print var 
   	continue 
	print "wont execute if var <3"
   else: break
   num = raw_input("Enter a number :")
   print "You entered :",num
else:
	print "Good bye!"

print("####use of while like single if stmt########")

while var==3:print "var ==3" #infinite loop
