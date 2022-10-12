"""
动态规划
https://www.bilibili.com/video/BV1XS4y1G7rs/?spm_id_from=autoNext&vd_source=751d83a470a7b7086d96d8b5dd5762d9
"""

nums = int(input())
heights = input().split(" ")
heights = list(map(int, heights))
left = [0 for i in range(nums)]
right = [0 for i in range(nums)]

for i in range(nums):
    j = nums - i - 1
    left[i] = 1
    for ii in range(i):
        if heights[i] > heights[ii]:
            left[i] = max(left[i], left[ii] + 1)
    right[j] = 1
    for jj in range(nums-1, j, -1):
        if heights[j] > heights[jj]:
            right[j] = max(right[j], right[jj] + 1)

min_removal = nums
for i in range(nums):
    removal = nums - (left[i] + right[i] - 1)
    min_removal = min(min_removal, removal)

print(min_removal)




