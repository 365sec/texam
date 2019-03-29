from itertools import count    
def isPrime(n):    
    if n <= 1:    
        return False   
    for i in count(2):    
        if i * i > n:    
            return True   
        if n % i == 0:    
            return False
list1=[]
for i in range(2,100):
	if isPrime(i) == True and isPrime(2**i-1) ==True:
		list1.append(2**i-1)
		if len(list1)>4:
			break
print(list1)
