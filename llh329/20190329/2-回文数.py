def hw(n):
    p=n
    k=0
    while p!=0:
        k=k*10+p%10
        p=p//10
    if k==n:
        return True
    else:
        return False
a=abs(int(input()))
print(hw(a))
