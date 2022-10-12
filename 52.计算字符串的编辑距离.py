"""
动态规划
插入：同行前列+1
删除：同列上行+1
替换：左上角斜对角线+1（不同）/左上角斜对角线+0（相同）
https://www.bilibili.com/video/BV1244y1J7Yw/?vd_source=751d83a470a7b7086d96d8b5dd5762d9
"""


word1 = input()
word2 = input()
dp = [[0 for i in range(len(word2)+1)] for i in range(len(word1)+1)]
for i in range(len(word1)+1):
    for j in range(len(word2)+1):
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i
        elif word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1)
for i in range(len(word1)+1):
    for j in range(len(word2)+1):
        print(str(dp[i][j])+" ", end=" ")
    print()
print(dp[len(word1)][len(word2)])
