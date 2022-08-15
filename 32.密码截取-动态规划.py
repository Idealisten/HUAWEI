password = input()
longest = 0
dp = [[False for i in range(0, len(password))] for j in range(0, len(password))]
for i in range(len(password)-1, -1, -1):
    for j in range(i, len(password)):
        if i == j:
            dp[i][j] = True
        elif 0 < j - i <= 2:
            if password[i] == password[j]:
                dp[i][j] = True
            else:
                dp[i][j] = False
        else:
            if password[i] == password[j] and dp[i+1][j-1]:
                dp[i][j] = True
            else:
                dp[i][j] = False
        if dp[i][j] and j+1-i > longest:
            longest = j+1-i
print(longest)
