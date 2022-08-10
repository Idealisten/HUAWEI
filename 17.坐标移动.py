coordinate = [0, 0]
str1 = input()
str1_list = str1.split(';')
for sub_str in str1_list:
    str_len = len(sub_str)
    if str_len > 3 or str_len < 2:
        pass
    else:
        direction = sub_str[0]
        steps = ""
        for i in range(1, str_len):
            if sub_str[i].isdigit():
                steps = steps + sub_str[i]
            else:
                steps = "-1"
                break
        steps = int(steps)
        if steps != -1:
            if direction == 'W':
                coordinate[1] += steps
            elif direction == 'S':
                coordinate[1] -= steps
            elif direction == 'A':
                coordinate[0] -= steps
            elif direction == 'D':
                coordinate[0] += steps

print(str(coordinate[0])+','+str(coordinate[1]))





