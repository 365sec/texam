import sys 
arr = input("")
num = [int(n) for n in arr[1:-1].split(",")]
arr1 = input("")
#arr1="['a', 'b', 'c']"
str1 = [n.strip()[1:-1] for n in arr1[1:-1].split(",")]

dest=[]
for i in range(len(num)):
	dest.append({num[i]:str1[i]})
   

print(dest)
