"""
暴力解法
"""

nums1 = input()
nums2 = input()
ans = 0
for i in range(len(nums1)):
    # print("i: {}".format(i))
    for j in range(len(nums2)):
        # print("j: {}".format(j))
        k = 0
        while i + k < len(nums1) and j + k < len(nums2) and nums1[i + k] == nums2[j + k]:
            # print("k: {}".format(k))
            k += 1

        ans = max(ans, k)


print(ans)
