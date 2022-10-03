"""
正则表达式
"""
import re
s = input()
N = int(input())
GC_MAX = 0
max_i = 0
for i in range(len(s)-N+1):
    sub_s = s[i:i+N]
    pattern = re.compile(r"[^CG]")
    sub_s = re.sub(pattern, "", sub_s)
    if len(sub_s) > GC_MAX:
        GC_MAX = len(sub_s)
        max_i = i

print(s[max_i:max_i+N])
