dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" %  dict.values()
print "###########################"
dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }

dict.update(dict2)
print "Value : %s" %  dict
print "###########################################"
dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" %  dict.setdefault('Age', None)
print "Value : %s" %  dict.setdefault('Sex', None)
print "##########################################"
dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" %  dict.keys()
print "###########################################"
dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" %  dict.items()
print "##############################################"
dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" %  dict.has_key('Age')
print "Value : %s" %  dict.has_key('Sex')
