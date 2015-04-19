print "###########reading the file and seek ###################"
fo = open("foo.txt", "r+")
str = fo.read(10);
print "Read String is : ", str

fid = fo.fileno()
print "File Descriptor: ", fid

# Check current position
position = fo.tell();
print "Current file position : ", position

print "##########Reposition pointer wrt to the  beginning of the file #####"
position = fo.seek(0, 0);
str = fo.read(10);
print "Again read String is : ", str

# Check current position
position = fo.tell();
print "Current file position : ", position

print "######Reposition pointer wrt the end of the file#########" 
position = fo.seek(-10, 2);
str = fo.read(5);
print "Again read String is : ", str

# Check current position
position = fo.tell();
print "Current file position : ", position

print "######Reposition pointer wrt to current position of the file#########"
position = fo.seek(-5, 1);
str = fo.read(5);
print "Again read String is,same as the above string: ", str

# Check current position
position = fo.tell();
print "Current file position : ", position



# Close opend file
fo.close()

