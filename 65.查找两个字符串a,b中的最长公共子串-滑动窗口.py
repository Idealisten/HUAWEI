nums1 = input()
nums2 = input()
max_len = 0
max_sub_nums: str = ""
max_len = 0
begin = len(nums1)
# 短的(len1)不动滑动长的(len2)
if len(nums1) > len(nums2):
    t = nums1
    nums1 = nums2
    nums2 = t
len1 = len(nums1)
len2 = len(nums2)
len_con = 1     # 重合部分长度

while len_con < len1:
    sub_nums1 = nums1[0:len_con]
    sub_nums2 = nums2[len2-len_con:len2]
    # print("len_con:{}".format(len_con))
    # print("sub_nums1:{}".format(sub_nums1))
    # print("sub_nums2:{}".format(sub_nums2))
    count = 0
    for i in range(len_con):
        if sub_nums1[i] == sub_nums2[i]:
            count += 1
            # print("count:{}".format(count))
            if count > max_len:
                max_len = count
                max_sub_nums = sub_nums1[i - max_len + 1:i + 1]
                begin = i - max_len + 1
            if count == max_len and i-max_len+1 < begin:
                max_sub_nums = sub_nums1[i-max_len+1:i+1]
                begin = i-max_len+1
                # print("max_len:{}".format(max_len))
                # print("max_sub_nums:{}".format(max_sub_nums))
                # print("begin:{}".format(begin))
        else:
            count = 0
    len_con += 1
    # print("")

mo = 0
while len_con + mo <= len2:
    sub_nums1 = nums1
    sub_nums2 = nums2[len2-len1-mo:len2-mo]
    # print("len_con:{}".format(len_con))
    # print("sub_nums1:{}".format(sub_nums1))
    # print("sub_nums2:{}".format(sub_nums2))
    count = 0
    for i in range(len_con):
        if sub_nums1[i] == sub_nums2[i]:
            count += 1
            # print("count:{}".format(count))
            if count > max_len:
                max_len = count
                ax_sub_nums = sub_nums1[i - max_len + 1:i + 1]
                begin = i - max_len + 1
            if count == max_len and i-max_len+1 < begin:
                max_sub_nums = sub_nums1[i-max_len+1:i+1]
                begin = i-max_len+1
                # print("max_len:{}".format(max_len))
                # print("max_sub_nums:{}".format(max_sub_nums))
                # print("begin:{}".format(begin))
        else:
            count = 0
    mo += 1
    # print("")

while len_con >= 1:
    sub_nums1 = nums1[len1-len_con:len1]
    sub_nums2 = nums2[0:0+len_con]
    # print("len_con:{}".format(len_con))
    # print("sub_nums1:{}".format(sub_nums1))
    # print("sub_nums2:{}".format(sub_nums2))
    count = 0
    for i in range(len_con):
        if sub_nums1[i] == sub_nums2[i]:
            count += 1
            # print("count:{}".format(count))
            if count > max_len:
                max_len = count
                max_sub_nums = sub_nums1[i - max_len + 1:i + 1]
                begin = i - max_len + 1 + len1 - len_con
            if count == max_len and i-max_len+1+len1-len_con < begin:
                max_sub_nums = sub_nums1[i-max_len+1:i+1]
                begin = i-max_len+1+len1-len_con
                # print("max_len:{}".format(max_len))
                # print("max_sub_nums:{}".format(max_sub_nums))
                # print("begin:{}".format(begin))
        else:
            count = 0
    len_con -= 1
    # print("")

# print(max_len)
# max_sub_nums = nums1[begin:begin+max_len]
print(max_sub_nums)
