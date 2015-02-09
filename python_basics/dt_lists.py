list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
list1 = ['\n'] #can not concatenate str with list and '\n' is just a listitem
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists
print (list + list1 +  tinylist) *2
print list[0:]      #same as print list

listnew = list + tinylist + list1
print listnew

list = list + tinylist #LIST IS NOT READONLY - NOT POSSIBLE WITH TUPLE
print list
