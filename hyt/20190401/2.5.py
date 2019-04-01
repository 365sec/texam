def judge(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
list = []
for i in range(2, 15):
    if not judge(i):
        continue
    elif not judge(2**i-1):
        continue
    else:
        list.append(2**i-1)
print(list)