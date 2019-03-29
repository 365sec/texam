# 2.合并数组
# ### Description
# 请以数组 a 中的元素为键（数组 a 中元素不重复），数组 b 中的元素为值，构建一个字典数组
# ### Specification
# 输入有两行，第一行为数组 a，第二行为数组 b，我们保证两个数组具有相同的元素个数。
# 输出为一个数组，数组中每一项为一个字典。
# ### Sample Input
# ```
# [1, 2, 3]
# ['a', 'b', 'c']
# ```
# ### Sample Output
# ```
# [{1: 'a'}, {2: 'b'}, {3: 'c'}]
# ```

a=input().strip('[]').split(',')
b=input().strip('[]').split(',')
aa = [int(n) for n in a]
bb = [m.strip()[1:-1] for m in b]
c=[]
for i in range(len(aa)):
    c.append({aa[i]:bb[i]})
print(c)