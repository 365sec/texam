# 7.回文数
# ### Description
# 回文数是指一个正读和反读都一样的数字。你能判断一个数字的绝对值是否是回文数吗？
# ### Specification
# 输入为一个整数 a
# 输出为 True 表示该数的绝对值是一个回文数, 反之为 False
# ### Sample Input
# ```
# 123
# 1221
# ```
# ### Sample Output
# ```
# False
# True
# ```

def issue():
    n=int(input())
    if n<0:
        n=-n
    m=str(n)[::-1]
    if str(m)==str(n):
        return True
    else:
        return False
x=issue()
print(x)
y=issue()
print(y)