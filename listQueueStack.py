list1 = []
list1.append("sadf")
list1.append(1)
list2 = []
list2.append(3)
list2.append(2)
list1.append(list2)
list1.insert(0,0)
print len(list1)
print 3 in list1
print list1
list1 +=list2
print list1
list2*=2
print list2
while(len(list1)>1):
    print list1[0]
    list1=list1[1:]

