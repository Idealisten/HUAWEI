"""
动态规划
A 、B数组各抽出一个前缀子数组，单看它们的末尾项，如果它们俩不一样——以它们俩为末尾项形成的公共子数组的长度为0：dp[i][j] = 0
如果它们俩一样，以它们俩为末尾项的公共子数组，长度保底为1——dp[i][j]至少为 1，要考虑它们俩的前缀数组——dp[i-1][j-1]能为它们俩提供多大的公共长度
如果它们俩的前缀数组的「末尾项」不相同，前缀数组提供的公共长度为 0——dp[i-1][j-1] = 0
以它们俩为末尾项的公共子数组的长度——dp[i][j] = 1
如果它们俩的前缀数组的「末尾项」相同
前缀部分能提供的公共长度——dp[i-1][j-1]，它至少为 1
以它们俩为末尾项的公共子数组的长度 dp[i][j] = dp[i-1][j-1] + 1
题目求：最长公共子数组的长度。不同的公共子数组的末尾项不一样。我们考察不同末尾项的公共子数组，找出最长的那个
dp[i][j] ：长度为i，末尾项为A[i-1]的子数组，与长度为j，末尾项为B[j-1]的子数组，二者的最大公共后缀子数组长度。
如果 A[i-1] != B[j-1]， 有 dp[i][j] = 0
如果 A[i-1] == B[j-1] ， 有 dp[i][j] = dp[i-1][j-1] + 1
base case：如果i==0||j==0，则二者没有公共部分，dp[i][j]=0
最长公共子数组以哪一项为末尾项都有可能，求出每个 dp[i][j]，找出最大值。
记录下找到dp[i][j]时的i值即为nums1公共子串的结尾位置
链接：https://leetcode.cn/problems/maximum-length-of-repeated-subarray/solution/zhe-yao-jie-shi-ken-ding-jiu-dong-liao-by-hyj8/
"""


nums1 = input()
nums2 = input()
if len(nums1) > len(nums2):
    t = nums1
    nums1 = nums2
    nums2 = t
len1 = len(nums1)
len2 = len(nums2)
end = 0
m = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]
ans = 0
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if nums1[i - 1] == nums2[j - 1]:
            m[i][j] = m[i - 1][j - 1] + 1
            if m[i][j] > ans:
                ans = m[i][j]
                end = i
                # print("ans:{}".format(ans))
                # print("end:{}".format(end))

# print(ans)
print(nums1[end-ans:end])



