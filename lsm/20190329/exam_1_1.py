#1.统计数字次数
# ### Description
# 给定一个数字字符串，请你统计每个数字出现的次数。
# ### Specification
# 输入为一个数字字符串，只包含 0-9 这 10 个数字
# 输出为一个包含10个数字的列表，分别为 0-9 每一个数字出现的次数
# ### Sample Input
# ```
# 12345678
# ```
# ### Sample Output
# ```
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
# ```
# ### Note
# 你可以使用 Counter

num=[0,0,0,0,0,0,0,0,0,0]
N=[int(x) for x in input()]
for i in range(len(N)):
    num[N[i]]+=1
print(num)