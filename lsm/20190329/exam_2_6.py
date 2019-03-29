# 6.回文串判断
# ### Description
# 判断一个字符串是否是回文串，所谓回文串就是指该字符串与其反序形式是一样。
# ### Specification
# 输入为一个字符串 s
# 如果 s 是回文串输出 True ，否则输出 False
# ### Sample Input
# ```
# AbA
# ```
# ### Sample Output
# ```
# True
# ```

def issue():
    a=input()
    b=a[::-1]
    if a==b:
        return True
    else:
        return False
a=issue()
print(a)