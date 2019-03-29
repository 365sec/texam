# 3.求集合的子集
# ### Description
# 请判断一个集合是否为另一个集合的子集
# ### Specification
# 输入为两行，分别为集合 set1 和 set2
# 输出为一个布尔值，如果 set1 是 set2 的子集，输出 True，否则输出 False
# ### Sample Input
# ```
# {1}
# {1, 2, 3}
# ```
# ### Sample Output
# ```
# True
# ```

def issue():
    a=input()[1:-1]
    b=[y for y in input()[1:-1].split(",")]
    if a in b:
        return True
    else:
        return False
c = issue()
print(c)