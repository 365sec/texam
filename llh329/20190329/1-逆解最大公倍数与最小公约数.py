arr = input("")
num = [int(n) for n in arr[1:-1].split(",")]

b=int(max(num))
a=int(min(num))
list1=[]
for i in range(a,b,a):
    for j in range(b,a,-a):
        if i*j==a*b:
            list1.append((i,j))
ss=1000
list2=[]
for k in list1:
    if ss>k[0]+k[1] and k[0]>a and k[1]<b and k[0]<k[1] :
        ss=k[0]+k[1]
        list2.insert(0,(k[0],k[1]))
print (list2[0])
