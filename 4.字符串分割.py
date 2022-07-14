str1 = input()
len1 = len(str1)

if len1 == 0:
    print(str1)

j = len1 % 8

if j != 0:
    str1 = str1 + '0' * (8-j)

for i in range(1, len(str1)+1):
    print(str1[i-1], end='')
    if i % 8 == 0:
        print('')