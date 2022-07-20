# 动态规划

n, m = map(int, input().split())
dp = [[0 for i in range(0, n+1)] for j in range(0, m+1)]


def steps_of_square(a, b):
    for i in range(0, b+1):
        for j in range(0, a+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[b][a]


print(steps_of_square(n, m))

