a = 10
b = 20
list1 = [1, 2, 3, 4, 5 ]; #string,list or tuple is possible

print list1

if ( 10 in list1 ):
   print  a,"is available in the given list"
else:
   print a," is not available in the given list"

if ( 20 not in list1 ):
   print b,"is not available in the given list"
else:
   print b,"is available in the given list"

a = 2
if ( 2 in list1 ):
   print a,"is available in the given list"
else:
   print a,"is not available in the given list"

#extra test ----- in and notin  oprtr with == try wd all tuple,list,tring,numbers etc - word string and sentence string - mixed list and tuple
print "#################################"
tuplemain = (123,"abcd",43434,"dfsdfs","fsdfsfsdfsd")
tuplesub = (123,"abcd",43434)
tuplesub_disorder = ("abcd",43434,123)
tuplesubsub = (123)
tuplesubsub_disorder = ("abcd")
#print tuplemain,tuplesub,tuplesub_disorder,tuplesubsub,tuplesubsub_disorder

if(tuplesub in tuplemain):
  print tuplesub,"in",tuplemain
else:
  print tuplesub,"not in",tuplemain
if(tuplesubsub in tuplemain):
  print tuplesubsub,"in",tuplemain
else:
  print tuplesubsub,"not in",tuplemain
if(tuplesubsub_disorder in tuplesub_disorder):
  print tuplesubsub_disorder,"in",tuplesub_disorder
else:
  print tuplesubsub_disorder,"not in",tuplesub_disorder
#conculsion : in and not in can be checked only with one item in a tuple
print "#################################################"
listmain = [123,"abcd",4567,"efghijk"]
listsub = [123,"abcd"]
listsub_disorder = ["abcd",4567]
listsubsub = [123]
listsubsub_disorder = ['abcd']
listsub_num = [123,4567]
mem_str = "efghijk"
mem_num = 4567
if(listsub_num in listmain):
  print listsub_num,"in",listmain
else:
  print listsub_num,"not in",listmain 
if(listsubsub in listsub):
  print listsubsub,"in",listsub
else:
  print listsubsub,"not in",listsub
if(listsubsub_disorder in listsub_disorder):
  print listsubsub_disorder,"in",listsub_disorder
else:
  print listsubsub_disorder,"not in",listsub_disorder
if(mem_num in listmain):
  print mem_num,"in",listmain
else:
  print mem_num,"not in",listmain 
if(mem_str in listmain):
  print mem_str,"in",listmain
else:
  print mem_str,"not in",listmain 

#in case of list we can only check number value(single) in or not in but incase of tuple u can check subtuple - only single member ......
