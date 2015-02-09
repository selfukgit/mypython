string = "2312123"
print int(string) #int(x [,base]) square brakcet items can be omitted
print int(string,10) #base 10
integer = 100
print hex(integer)  #output is hex string
print oct(integer)  #output is oct string
print chr(integer)  #output is character
print unichr(integer) #output is character

list1 = ["ab", 123]
tuple1 = ["ef",456]
print tuple(list1)
print list(tuple1)
#print dict(tuple1) #both doesnt work
#print dict(list1)
print dict([('a',1),('b',2),("c","c")])
