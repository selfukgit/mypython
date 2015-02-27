a = 0
b = 1
c = 2
	
d = c<<a|a>>c&a+b
print d
print "Precedence +,>>/<<,&,| ======> 10<<0|0>>2&0+1 = 10<<0|0>>10&01 = 10<<0|0>>0 = 10<<0 = 10 = 2(decimal)"
