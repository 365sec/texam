arr1 = input("")
#arr1="['a', 'b', 'c']"
str1 = {n for n in arr1[1:-1].split(",")}
arr2 = input("")
#arr1="['a', 'b', 'c']"
str2 = {n for n in arr2[1:-1].split(",")}
if len(str1)<=len(str2):
	if str1&str2==str1:
		print(True)
	else:
		print(False)
else:
		print(False)
