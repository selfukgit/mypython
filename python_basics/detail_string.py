#!/usr/bin/pythonstr = "0000000this is string example....wow!!!0000000";
#!/usr/bin/python


str = u"this2009";  
print str.isdecimal();

str = u"23443434";
print str.isdecimal();
print "###########################################################"
str = "this is string example....wow!!!";

print str.zfill(40);
print str.zfill(50);
print "#########################################################"
from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab, 'xm');

print " ##################################################"
str = "this is string example....wow!!!";
print str.swapcase();

str = "THIS IS STRING EXAMPLE....WOW!!!";
str1 = str.swapcase();

print str1.swapcase();
print "###################################################"
str = "0000000this is string example....wow!!!0000000"
print str.strip( '0' )
str = "this is string example....wow!!!";
print str.strip( 't' )
print "##################################################"
str = "this is string example....wow!!!";
print str.startswith( 'this' );
print str.startswith( 'is', 2, 100 );
print str.startswith( 'this', 0);
print "###################################################"
str = "Line1-a b c d e f\nLine2- a b c\nLine4- a b c d\n\n";
print str.splitlines( );
print str.splitlines( 0 );
print str.splitlines( 3 );
print str.splitlines( 4 );
print str.splitlines( -1 );

print "##################################################"
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );
print str.split('\n', 1);
print "####################################################"

str = "     this is string example....wow!!!     ";
print str.rstrip();
str = "88888888this is string example....wow!!!8888888";
print str.rstrip('8');
str = "88888888this is string example....wow!!!8888888";
print str.rstrip('!');
print "#####################################################"


var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0];
print "var2[1:5]: ", var2[1:5]

#we can update python string not like C - string is not constant 
var1 = 'Hello World!'

print "Updated String :- ", var1[:6] + 'Python'
print "Updated String again : -",var1[:0] + "hai how are you"
print "Updated String again :-",var1[:2] + "python"

a = 'Hello'
b = 'Python'

print"a+b =",a+b
print"2*b = ",2*b
#print "a[100] = ",a[100]
print "a[3] = ",a[3]
print "a[1:4] = ",a[1:4]
print "H in a =",'H' in a
print "M not in a = ",'M' not in a
print r"dkvskdv\ndfvdfvd"
print R"dcsdcsdcsc\nsfvsdvsdv"

print "My name is %s and weight is %d kg!" % ('Zara', 21)

print "caasas*dscsdc-csdcsd+< >421412"

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print para_str

print 'C:\\nowhere'
print r'C:\\nowhere'

print u'Hello, world!'
print "Hello, world!"

str = "this is string example....wow!!!";

print "str.capitalize() : ", str.capitalize()

str = "this is string example....wow!!!";


str = "this is string example....wow!!!";

print "str.center(40, 'a') : ", str.center(45, 'a')

str = "this is string example....wow!!!";
str = str.encode('base64','strict');

print "Encoded String: " + str;
print "Encoded String: ",str
print "Decoded String: " + str.decode('base64','strict')

str = "this is string example....wow!!!";

suffix = "wow!!!";
print str.endswith(suffix);
print str.endswith(suffix,30);

suffix = "is";
print str.endswith(suffix, 2, 4);
print str.endswith(suffix, 2, 6);

str = "this is\tstring example....wow!!!";


print "Original string: " + str;
print "Defualt exapanded tab: " +  str.expandtabs();
print "Double exapanded tab: " +  str.expandtabs(16);

str1 = "this is string example....wow!!!";
str2 = "exam";

print str1.index(str2);
print str1.index(str2, 10);
# print str1.index(str2, 40) : gives exception

str1 = "this is string example....wow!!!";
str2 = "exam";

print str1.find(str2);
print str1.find(str2, 10);
print str1.find(str2, 40);

str = "this2009";  # No space in this string
str1 = "23721731023712"
print str.isalnum();
print str1.isalnum()

str = "this is string example....wow!!!";
print str.isalnum();


str = "this";  # No space & digit in this string
print str.isalpha();

str = "this is string example....wow!!!";
print str.isalpha();

print"############################"

str = u"this2009";  
print str.isnumeric();

str = u"23443434";
print str.isnumeric();

print"####################################################"
str = "@#$##";
seq = ("a", "b", "c"); # This is sequence of strings.
print str.join( seq );

print "###########################################"
str = "this is string example....wow!!!";

print str.ljust(50, '0');

print "##############################"
str = "     this is string example....wow!!!     ";
print str.lstrip();
str = "88888888this is string example....wow!!!8888888";
print str.lstrip('t');
print str.lstrip('8')

print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
intab = "aeiou"
outtab = "12345"
#trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
#print str.translate(trantab);
print "######################################"
str = "this is really a string example....wow!!!"
str1 = "is"

print str.rfind(str1)
print str.rfind(str1, 0, 10)
print str.rfind(str1, 10, 0)

print str.find(str1)
print str.find(str1, 0, 10)
print str.find(str1, 10, 0)

print str.find(str1)
print str.find(str1, 0, 10)
print str.find(str1, 10, 0)

print "######################################"

str = "this is string example....wow!!!";

print str.rjust(50, '0')
print str.rjust(10,'0') #original string is returned if width less than the len(# - )
print "###################################################"
