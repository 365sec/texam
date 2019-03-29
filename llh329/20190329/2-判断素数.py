import sys 
from itertools import count    
def isPrime(n):    
    if n <= 1:    
        return False   
    for i in count(2):    
        if i * i > n:    
            return True   
        if n % i == 0:    
            return False   

try:
	for line in sys.stdin: 
		a=int(line) 
		print(isPrime(a))
except EOFError:
    pass

