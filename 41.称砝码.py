"""
我们可以先从砝码比较少的情况开始想：只有2两个1g砝码和1个2g砝码能组成多少种？

首先0肯定是一种；
使用1个1g加上现有的0g构成一种；
使用1个1g加上现有的0g重复了，使用1个1g加上现有的1g构成2g；
使用1个2g加上现有的0g重复了，使用1个2g加上现有1g构成3g，使用1个2g加上现有的2g构成4g；
在砝码种类和数量都比较多的时候，我们也可以从0g开始，遍历每一种的重量的砝码的每一个（即遍历每个砝码），对当前集合种所有的种类都加上这个重量，如果重复则去除，否则加入。
"""

n = int(input())
m = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

# sumlist = [0]
sumset = {0}

for i in range(n):
    for j in range(x[i]):
        # for k in sumlist.copy():
        sumset2 = sumset.copy()
        for k in sumset2:
            # if k + m[i] not in sumlist:
            if k + m[i] not in sumset2:
                # sumlist.append(k+m[i])
                sumset.add(k+m[i])

# print(len(sumlist))
print(len(sumset))

