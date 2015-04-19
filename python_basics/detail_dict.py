
dict = {'Name': 'Zara', 'Age': 27}

print "Value : %s" %  dict.get('Age')
print "Value : %s" %  dict.get('Sex', "default value to be returned as key name sex is not available")
print "###############################################"
seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print "New Dictionary : %s" %  str(dict)

dict = dict.fromkeys(seq, 'dqwdqd')
print "New Dictionary : %s" %  str(dict)
print "##################################################"
dict1 = {'Name': 'Zara', 'Age': 7};

dict2 = dict1.copy()
print "New Dictinary : %s" %  str(dict2)
print "##################################################"
dict = {'Name': 'Zara', 'Age': 7};

print "Start Len : %d" %  len(dict)
dict.clear()
print "End Len : %d" %  len(dict)

print "#################################################"
dict1 = {'Name': 'Zara', 'Age': 7};
tupe = (50,)
print "Variable Type : %s" % type(tupe)
print "#################################################"
dict = {'Name': 'Zara', 'Age': 7};
print "Equivalent String : %s" % str (dict)
print "###########################################################"
dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = {'Name': 'Mahnaz', 'Age': 27};
dict3 = {'Name': 'Abid', 'Age': 27};
dict4 = {'Name': 'Zara', 'Age': 7};
print "Return Value : %d" %  cmp (dict1, dict2)
print "Return Value : %d" %  cmp (dict2, dict3)
print "Return Value : %d" %  cmp (dict1, dict4)
#dict compare - first they compare values if they are different then sort accordingly ....if values r same then compare key string and each literals................ still complications are there ......................if you change age to string and incase of more number of dict items
print " #############################################"
dict1 = {'Name': 'scascZdcascasc', 'Age': 10};
dict2 = {'Name': 'cascZcscasc', 'Age': 11};
dict3 = {'Name': 'scZbcascas', 'Age': 12};
dict4 = {'Name': 'scaZacsasca', 'Age': 13};
print "Return Value : %d" %  cmp (dict1, dict2)
print "Return Value : %d" %  cmp (dict2, dict3)
print "Return Value : %d" %  cmp (dict1, dict4)
print "####################################################"
#dict = {['Name'] : 'uk'} #not allowed list as it is mutable
#dict
dict = {('Name'):'uk'}#allowed as tuple is mutable
#dict = {('name','name1'):'uk'} #not allowed with [] bracket 
print dict,dict['name'],dict['name1']
print "##########################################################"
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};

print "dict['Name']: ", dict['Name'];

print "++++++++++++++++++++++++++++++++++++++++++++++++++++++"
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

del dict['Name'] # remove entry with key 'Name'
print dict
dict.clear()     # remove all entries in dict
print dict
del dict ;        # delete entire dictionary
print dict

#print "dict['Age']: ", dict['Age'];
#print "dict['School']: ", dict['School'];
print "#################################################"
dict1 = { 'abc': 456 };
dict2 = { 'abc': 123, 98.6: 37 };
dict3 = {'key1': 1,'key2':2,'key3' :2}

dict3['key1'] = 100
dict3['key4'] = 1000

print dict1,dict2,dict1['abc'],dict2[98.6],dict3
