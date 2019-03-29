# 5.默尼森数
# ### Description
# P是素数且M也是素数，并且满足等式M=2^P - 1，则称M为默尼森数。例如，P=5， M=2^P - 1 = 31，
# 5和31都是素数，因此31是默尼森数。编写判断素数的函数并找出前5个默尼森数。
# ### Specification
# 输出前五个默尼森数到列表中
# ### Sample Output
# ```
# [3, ...]
# ```

import math
def issue(n):
    k = int(math.sqrt(n))+1
    if n<=1:
        return False
    for i in range(2,k):
        if n%i==0:
            return False
    return True
z=0
num=[]
for x in range(2,20):
    y = 2**x-1
    if issue(x)==True and issue(y)==True:
        num.append(y)
        z+=1
        if z == 5:
            break
        else:
            pass
    else:
        pass
print(num)