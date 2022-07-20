m, n = map(int, input().split())


def func(a, b):
    # 苹果是a行，盘子是b列
    dp = [[0 for x in range(0, b + 1)] for y in range(0, a + 1)]
    # 先循环苹果（行），再循环盘子（列）
    for i in range(0, a+1):
        for j in range(1, b+1):
            if i == 0 or i == 1 or j == 1:
                dp[i][j] = 1
            else:
                if i < j:
                    dp[i][j] = dp[i][i]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-j][j]
    print(dp)
    print(dp[a][b])


func(m, n)
