# 6.逆解最大公倍数与最小公约数
# ### Description
# 我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。
# 今天我们反其道而行之，给你两个数 a 和 b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
# ### Specification
# 输入为一个元组 (gcd, lcm) 表示两个数的最大公约数和最小公倍数（ 0 < gcd < lcm < 10^8 ）
# 输出一个元组表示这两个数，小的在前，大的在后（若有多组解，输出它们之和最小的那组）。
# ### Sample Input
# ```
# (3, 60)
# ```
# ### Sample Output
# ```
# (12, 15)
# ```

import math
z = eval(input())
a=int(min(z[0],z[1]))
b=int(max(z[0],z[1]))
d=int(b/a)
k = int(math.sqrt(d)) +1
XYList=[(i,int(d/i))for i in range(k, 0,-1) if d%i ==0]
XYList =[i for i in XYList if math.gcd(i[0],i[1])==1]
XYList.sort(key = lambda i:i[0]+i[1])
x=min(XYList[0][0],XYList[0][1])*a
y=max(XYList[0][0],XYList[0][1])*a
print((x,y))