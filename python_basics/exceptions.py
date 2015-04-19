try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "IOError: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fh.close()
print "#######use of finally##################"
try:
   fh = open("testfile", "r")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print "Going to close the file"
      fh.close()
except IOError,arg:
   print "Error: can\'t find file or read data,arg : ",arg
