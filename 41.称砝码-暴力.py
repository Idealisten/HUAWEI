"""
穷举法：把砝码一个个放到 lst=[n1,n1,n1,n2,n2,n2,...]，
然后按照取1个、取2个。取m*n个，依次求和，把和不重复的放到sumlist中。这样数据量太大会超时
"""
from itertools import combinations

n = int(input())
m = [int(i) for i in input().split(" ")]
x = [int(i) for i in input().split(" ")]

lst = []
# lst存所有砝码，一个位置放一个砝码，总如砝码1有2个，砝码2有3个，则lst=[m1,m1,m2,m2,m2]
for i in range(n):
    for j in range(x[i]):
        lst.append(m[i])

sumlist = [0]

for i in range(1, len(lst)+1):
    for j in set(combinations(lst, i)):
        # 分别取一个砝码、二个砝码。。计算和是否相同，不同的放到sumlist中
        if sum(j) not in sumlist:
            sumlist.append(sum(j))
            # j是一个元组，元组的和是所选砝码质量的和
print(len(sumlist))

