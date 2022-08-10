"""
一个旅行者有一个最多能装M公斤的背包，现有n件物品，重量分别是W1，W2…，价值分别是C1，C2…，求旅行者能获得的最大总价值
输入：
第一行输入两个整数M(背包容量<=200)和N(物品数量<=30)，
第2…N行：每行两个整数Wi和Ci，表示每个物品的重量和价值
输出：
一行，一个数，表示最大总价值吗
"""

# 横坐标代表当前容量j，纵坐标代表第i物品
m, n = map(int, input().split())
dp = [[0 for j in range(m+1)] for i in range(n+1)]
w = [0]*35
c = [0]*35

for i in range(1, n+1):
    w[i], c[i] = map(int, input().split())

# 先遍历横坐标容量，后遍历纵坐标第几物品
for i in range(1, n+1):
    for j in range(1, m+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + c[i])

# 输出dp表
for d in dp:
    print(d)

