import sys

def judge(num):
    if num<=1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

try:
    for item in sys.stdin:
        print (judge(int(item.strip())))
except:
    pass