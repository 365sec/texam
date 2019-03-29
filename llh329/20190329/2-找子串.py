def search(s1,s2):
    sum = 0
    for i in range(0,len(s1)):
        str = s1[i:]
        if(str.find(s2) == 0):
            sum += 1
        else:
            continue
    return sum
             

s1 = input()
s2 = input()
print(search(s1,s2))