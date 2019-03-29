# 7.水果出售记录
# ### Description
# 某水果店简单地把每天销售的水果记录在一个列表中，你能帮忙店老板统计出每个水果卖出了多少，并从多到少排个序吗？
# ### Specification
# 输入为一个字符串列表，每项为一个水果的名字。
# 输出为一个列表，每一项为一个二元组表示水果和卖出数量，列表需要按照水果的卖出数量从多到少排序，如果数量相同就按照水果名称
# 在列表中的先后顺序排列。
# ### Sample Input
# ```
# ['apple','banana','cherry','pineapple','banana']
# ```
# ### Sample Output
# ```
# [('banana', 2), ('apple', 1), ('cherry', 1), ('pineapple', 1)]
# ```
# ### Note
#
# 你可以使用 Counter

import collections
obj = collections.Counter(eval(input()))
print(obj.most_common())