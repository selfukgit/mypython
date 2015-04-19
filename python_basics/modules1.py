import sys
print "######################dir() func ###############################"
content = dir(sys)
print content
print "#############global and local variables and globals() & locals()#############################"
Money = 2000
dicglobalin = { 'name' : 'name'}
diclocalin = { 'name' : 'name'}
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money #this statement tells that Money is a global variable 
   Money = Money + 1
   dicglobalin = globals()
   dictlocalin = locals()
   print "inside function globals,locals",dicglobalin,diclocalin

print Money
AddMoney()
print Money
dicglobalin = globals()
dictlocalin = locals()
print "outside the function globals,locals",dicglobalin,diclocalin

print " #############printing the value of PYTHONPATH #############################"
print (sys.path) #Printing the value of PYTHONPATH 
