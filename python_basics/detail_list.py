
aList = [123, 'xyz', 'zara', 'abc', 'xya'];

aList.sort();
print "List : ", aList;
print "##############################################"
aList = [123, 'xyz', 'zara', 'abc'];

print "A List : ", aList.pop();
print "B List : ", aList.pop(2);
print aList 
print "##############################################"
aTuple = (123, 'xyz', 'zara', 'abc');
aList = list(aTuple)

print "List elements : ", aList
print "##############################################"
list1, list2 = [123, 'xyz', 'zara', 'abc','zzz','ZZZ'], [456, 700, 200,'zzz']
list = ['abc',123]
print "Max value element : ", max(list);
print "Min value element : ", min(list);

print "Max value element : ", max(list1);
print "Max value element : ", max(list2);
print "##########################################"
list1, list2 = [123, 'xyz'], [456, 'abc']

print cmp(list1, list2);
print cmp(list2, list1);
list3 = list2 + [786];
print list3
print cmp(list2, list3)

list1, list2 = ['xyz',123], ['abc',456]

print cmp(list1, list2);
print cmp(list2, list1);
list3 = list2 + [786];
print list3
print cmp(list2, list3)


print "##############################################"
L = ['spam0', 'Spam1', 'SPAM!2']
print "L[-2] :",L[-2]
print "L[-3] :",L[-3]
print "L[-1] :",L[-1]
print L[0],L[1],L[2]
#vm concept above ................. 2,1,0 0,1,2
print "##############################################"
list = ['physics', 'chemistry', 1997, 2000];

print "Value available at index 2 : "
print list[2];
list[2] = 2001;
print list
print "New value available at index 2 : "
print list[2];
list.append('sdasdas')
print list
del list[0]
print list
list.remove(2001)
print list

print "##################################"
print "len([1, 2, 3]):",len([1, 2, 3])
print "[1, 2, 3] + [4, 5, 6]:",[1, 2, 3] + [4, 5, 6]
print "['Hi!'] * 4 :",['Hi!'] * 4
print "3 in [1, 2, 3]:",3 in [1, 2, 3]
for x in [1, 2, 3]: print "for x in [1, 2, 3]",x
