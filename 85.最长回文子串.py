"""
动态规划
如果str长度为1，是回文串
如果str长度为2，如果首尾字符相同，是回文串
如果str长度大于2，如果首尾字符不相同，不是回文串；如果相同，取决于去掉首尾字符的子串是否为回文串，dp[i][j] = dp[i+1][j-1]
dp[i][j]代表str的子串str[i:j+1]是否为回文串
https://www.bilibili.com/video/BV11u41197sj/?spm_id_from=333.788.recommend_more_video.3&vd_source=751d83a470a7b7086d96d8b5dd5762d9
"""

astr = input()
dp = [[0 for i in range(len(astr))] for j in range(len(astr))]
max_length = 1
astr_length: int = len(astr)


if astr_length < 2:
    print()

begin = 0
for i in range(astr_length):
    dp[i][i] = 1

for sub_length in range(2, astr_length+1):
    for i in range(0, astr_length-sub_length+1):
        j = i + sub_length - 1
        if astr[i] == astr[j]:
            if sub_length < 3:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i+1][j-1]
        else:
            dp[i][j] = 0

        if dp[i][j] == 1 and sub_length > max_length:
            max_length = sub_length

print(max_length)





