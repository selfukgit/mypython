#to print prime numbers given in certain limit
ll =int( raw_input("Enter lower limit >0 : \n"))
ul = int(raw_input("Enter upper limit : \n"))
for num in range(ll,ul):
	#print"##########################################"
	divisor = 2
	#print "num =%d"%(num) #testing % usage
	while(divisor < num):
	 	#print"divisor = ",divisor
		if num%divisor == 0:
			j = num/divisor
			#print"%d equals %d * %d"%(num,divisor,j)
			break #goes to for loop/first loop
		divisor = divisor + 1
	else:
		if num >1:print num #print prime numbers ie num >1
		#print num,"is a prime"
	
