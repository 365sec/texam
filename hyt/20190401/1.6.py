import math
def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)

a = eval(input())
mxm = a[0]*a[1]
div = a[1]//a[0]
list = []
for i in range(1, int(div**0.5)+1):
    for j in range(int(div**0.5), div+1):
        if i*j == div and gcd(i, j) == 1:
            list.append((i*a[0], j*a[0]))
print (list[-1])