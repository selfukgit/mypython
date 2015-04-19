print "###############file opening ######################"
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
print "####################input()########################"
str = input("Enter your input,enter with square bracket as a list:\n ");
print "Received input is : ", str
print "########raw_input#######################"
str = raw_input("Enter the string\n")
print "received input:",str
print "###################multiple prints##############"
print "hai","hai1","hai2"
