#numbers
var1 = 100
var2 = 100.1
var_signed = -234.345 #signed float,int in python is signed int
print var1,var2
#del var1
#print var1,var2 #gives var1 not defined error
del var1,var2
#print var1,var2
print var_signed

varint1 = 80
varint2 = -490
varint3 = -0x260
varlong1 =-343434234L #even small 'l' is also supported but do not use as it would confuse with '1'
varlong2 = -233423423l #permits 'l' too
varlong3 = -0xDEFFFFFFFFFFFFFL
varlong4 = 0xFFEd
varlong5 = 0xeeffl#ignores l,as it is required to notify that this is long,same way in varlong3 too 'L'
varfloat1 = -23423324.4124124123
varfloat2 = 45.6e45
#varfloat3 = 2323+E232 #here capital E is not defined use only small e
varfloat3 = 2323e23
varfloat4 = 23.4e+45 #different notation
varcomplex1 = 3.4j
varcomplex2 = 45.6J
varcomplex3 = -345.45-456.5j
print '#######'
print varint1,varint2,varint3
print varlong1,varlong2,varlong3,varlong4,varlong5
print varfloat1,varfloat2,varfloat3,varfloat4
print varcomplex1,varcomplex2,varcomplex3
