s = input()
dict_a = dict()
flag = -1

for char in s:
    if char not in dict_a:
        dict_a[char] = 1
    else:
        dict_a[char] = dict_a[char] + 1

for key, value in dict_a.items():
    if value == 1:
        print(key)
        flag = 0
        break

if flag != 0:
    print(flag)

