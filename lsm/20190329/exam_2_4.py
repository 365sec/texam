# 4.找子串
# ### Description
# 对于字符串 s1，统计在字符串 s1 中另一个字符串 s2 出现的次数
# ### Specification
# 输入为两个字符串 s1 和 s2
# 输出为 s2 在 s1 中的出现次数
# ### Sample Input
# ```
# AABBAACC
# BB
# ```
# ### Sample Output
# ```
# 1
# ```

a = input()
b = input()
x=0
for i in range(len(a)):
    if a[i:].find(b)==0:
        x+=1
print(x)