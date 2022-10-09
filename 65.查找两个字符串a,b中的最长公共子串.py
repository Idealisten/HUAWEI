"""
暴力解法，注意要把较短的字符串放在外层循环，否则在有相同长度子串时只会记录较长字符串中第一个出现的
"""
str1 = input()
str2 = input()
if len(str1) > len(str2):
    t = str1
    str1 = str2
    str2 = t
ans = 0
begin = 0
length = 0
for i in range(len(str1)):
    for j in range(len(str2)):
        k = 0
        while i + k < len(str1) and j + k < len(str2) and str1[i + k] == str2[j + k]:
            k += 1
        if k > ans:
            ans = k
            begin = i
            length = k
print(str1[begin:begin+length])
