str1 = "nvlrzqcjltmrejybjeshffenvkeqtbsnlocoyaokdpuxutrsmcmoearsgttgyyucgzgcnurfbubgvbwpyslaeykqhaaveqxijc"
str2 = "wkigrnngxehuiwxrextitnmjykimyhcbxildpnmrfgcnevjyvwzwuzrwvlomnlogbptornsybimbtnyhlmfecscmojrxekqmj"
ans = 0
begin = []
length = []
print(len(str1))
print(len(str2))
for i in range(len(str1)):
    for j in range(len(str2)):
        k = 0
        while i + k < len(str1) and j + k < len(str2):
            if str1[i + k] == str2[j + k]:
                k += 1
        if k > ans:
            ans = k
            if len(str1) < len(str2):
                begin.append(i)
                length.append(k)
                print("sub_str1:{}".format(str1[i:i+k]))
            else:
                begin.append(j)
                length.append(k)
                print("sub_str2:{}".format(str2[j:j+k]))
            print("ans:{}".format(ans))


# if len(str1) < len(str2):
#     print(str1[begin:begin+length])
# else:
#     print(str2[begin:begin+length])
