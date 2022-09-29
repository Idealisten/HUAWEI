"""
暴力解法
双层循环
"""
s = input()
N = int(input())
GC_MAX = 0
max_i = 0
for i in range(len(s)-N+1):
    sub_s = s[i:i+N]
    GC = 0
    for char in sub_s:
        if char == "G" or char == "C":
            GC += 1
    if GC > GC_MAX:
        GC_MAX = GC
        max_i = i

print(s[max_i:max_i+N])
