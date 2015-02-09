dict1 = {}
list1 = ['list1',1]
tuple1 = ("tuple one",1)
#key can be number or string
dict1["1st key"] = list1
dict1[2] = tuple1

print dict1 #elements are printed disorded

#editing dict1 items
dict1["""3rd key"""] = 3 #note """ - doest issue any problem
print dict1
#editing the already entered key-value is possible in dict -not readonly
#list1[2] = "second element" #index out of error gets - not possible to extend
list1[1] = "second element"
dict1[2] = list1
print dict1

print dict1['1st key']
print dict1[2]
print dict1["3rd key"]
print dict1.keys()
print dict1.values()
tinydict = {"name" :1234,'code':3456,"address":"""address"""}
print tinydict
print tinydict.keys()
print tinydict.values()
