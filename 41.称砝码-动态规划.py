"""
我们可以先计算出所有砝码总重量，然后用长为总重量sum+1sum+1sum+1的bool型的dp数组计算每种重量是否可能出现，最后遍历这个dp数组统计每种重量出现的次数。
首先dp[0]=1dp[0]=1dp[0]=1，然后我们遍历每个砝码（即每种重量的每一个），每次从sum开始往下递减，如果该重量k减去当前遍历到的这个砝码的重量得到的那个重量已经出现了即已经被别的组装好了，那我们就认为这个重量可以出现，置为1.
"""
n = int(input())
m = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

sum_m = 0
for i in range(len(m)):
    sum_m += m[i] * x[i]

dp = [0 for i in range(sum_m+1)]
dp[0] = 1

for i in range(n):  # 遍历每一种砝码
    for j in range(x[i]):   # 遍历每一种砝码的数量
        for k in range(sum_m, m[i]-1, -1):
            if dp[k] != 1:
                if dp[k-m[i]] == 1:
                    dp[k] = 1

print(sum(dp))
