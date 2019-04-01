a = input()
def jugde(string):
    length = len(string)
    for i in range(length//2):
        if string[i]!=string[-i-1]:
            return False
    return True
print(jugde(a))
