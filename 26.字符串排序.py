str1 = input()
list1 = list(str1)
list2 = []

for i in range(26):
    # 每轮循环判断一个字母，共需要26轮循环
    for j in list1:
        if ord(j) == ord('a')+i or ord(j) == ord('A')+i:
            list2.append(j)
# print(list2)
x = 0
for k in list2:
    while not('a' <= list1[x] <= 'z' or 'A' <= list1[x] <= 'Z'):
        # 如果不是字母需要将坐标+1
        x += 1
    list1[x] = k
    x += 1


str1 = "".join(list1)
print(str1)


