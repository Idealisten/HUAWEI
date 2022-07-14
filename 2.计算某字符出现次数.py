# str1 = input()
# str2 = input()
# count = 0
# for i in range(0, len(str1)):
#     if 65 <= ord(str2) <= 90 or 97 <= ord(str2) <= 122:
#         if str1[i] == str2 or abs(ord(str1[i])-ord(str2)) == 32:
#             count += 1
#     else:
#         if str1[i] == str2:
#             count += 1
# print(count)

# 如果是字母才需要考虑大小写，如果不是字母不需要考虑大小写

str1 = input()
str2 = input()
print(str1.lower().count(str2.lower()))
