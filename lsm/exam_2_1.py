# 1.判断素数
# ### Description
# 判断一个数是否是素数。素数又叫质数，它是一个大于1的自然数，除了1和它自身外，不能整除其他自然数。
# ### Specification
# 输入为 a (0 < a < 10^13)
#
# 输出为 True 表示 a 是一个素数, 否则输出 False
# ### Sample Input
# ```
# 4
# 17
# ```
# ### Sample Output
# ```
# False
# True
# ```

import math
def issue():
    n=int(input())
    k = int(math.sqrt(n))+1
    if n<=1 or n>=10**13:
        return False
    for i in range(2,k):
        if n%i==0:
            return False
    return True
a=issue()
print(a)