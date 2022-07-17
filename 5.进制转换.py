import math

num0x = input()
num0x = num0x[2:]
len_num0x = len(num0x)
dec_sum = 0
for i in range(len_num0x - 1, -1, -1):
    if ord('0') <= ord(num0x[i]) <= ord('9'):
        dec_sum = dec_sum + \
            (ord(num0x[i]) - ord('0')) * pow(16, len_num0x - 1 - i)
    else:
        dec_sum = dec_sum + \
            (ord(num0x[i]) - ord('A') + 10) * pow(16, len_num0x - 1 - i)
print(dec_sum)

#  用和'0'或'A'的ASCII码的差值来确定当前位的十进制数
