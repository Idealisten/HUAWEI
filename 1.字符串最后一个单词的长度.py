astr = input()
i = len(astr) - 1
letter = astr[len(astr) - 1]
while letter != ' ' and i >= 0:
    i = i - 1
    letter = astr[i]
print(len(astr) - 1 - i)

# 有可能此字符串没有空格
