arr = input("")
num = [int(n) for n in arr[1:-1].split(",")]
def f(x):
    return x+10
print (list(map(f,num)))
