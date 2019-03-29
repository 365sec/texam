# 3.试一试map函数
# ### Description
# map函数是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，
# 得到一个新的 list 并返回。
# ### Specification
# 输入为一个数组 L，数组中每个元素都是数字
# 输出为一个数组 L1，L1是数组 L 对应位置元素加上 10
# ### Sample Input
# ```
# [1, 2, 3]
# ```
# ### Sample Output
# ```
# [11, 12, 13]
# ```

a=input().strip('[]').split(',')
aa = list(map(lambda x:x+10,[int(n) for n in a]))
print(aa)