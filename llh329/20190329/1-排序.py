arr = eval(input(""))
list1=[]
for i in arr:
	list1.append(int(i))
list2=[]
list2.append(list1[0])


for i in range(1,len(list1)):
	key=0
	for s in range(0,len(list2)):
		if list1[i]<list2[s]and key==0:
			list2.insert(s,int(list1[i]))
			key=1
	if key==0:
		list2.insert(len(list2),int(list1[i]))
		key=0
list3=[]
for i in list2:
    list3.append((i))
print (list3)
