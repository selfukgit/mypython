import mod_arithmetic 
#import mod_from

from mod_from import sample_print 

print mod_arithmetic.sample_add_print(10,20)
print mod_arithmetic.sample_multiply_print(10,20)

print sample_print(10) #no need to write mod_from.sample_print(10)
print sample_print2() #will give error as it is not imported
