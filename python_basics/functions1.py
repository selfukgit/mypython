print "###############variable length arguments ##########################"

def printvariable(*vartuple):
        "This function prints a variable number of arguments"
        #print arg1
        for var in vartuple:
                print var
                #return
#if there is no return then we can leave return stmt    

#calling printvariable
printvariable() #calling without any arguments
print "#######" 
printvariable(10)
printvariable(10,-2,3,4,567)

