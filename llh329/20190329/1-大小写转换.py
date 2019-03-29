import re
a=input()
s=""
for i in a:
    if i.isupper() == True :
        i=i.lower()
    else:
        i=i.upper()
    s=s+i
print (s)
