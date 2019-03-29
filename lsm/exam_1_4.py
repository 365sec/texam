# 4.排序
# ### Description
# 给一个整数序列排序
# ### Specification
# 输入为一个整数数组 a
# 输出为给 a 按元素从小到大排序后的数组
# ### Sample Input
# ```
# [3, 1, 2]
# ```
# ### Sample Output
# ```
# [1, 2, 3]
# ```

def issue():
    x = eval(input())
    for i in range(1,len(x)):
        for j in range(0,len(x)-i):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x
y = issue()
print(y)