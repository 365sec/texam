import sys
def jugde(string):
    length = len(string)
    for i in range(length//2):
        if string[i]!=string[-i-1]:
            return False
    return True

# a = raw_input()
# print jugde(str(abs(int(a))))
try:
    for item in sys.stdin:
        print (jugde(str(abs(int(item)))))
except:
    pass