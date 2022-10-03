"""
双指针
"""

s = input()
N = int(input())
GC_MAX = 0
max_i = 0
GC = 0
for i in range(N):
    if s[i] == "G" or s[i] == "C":
        GC += 1
GC_MAX = GC

for i in range(1, len(s)-N+1):
    j = i + N - 1
    if s[i-1] == "G" or s[i-1] == "C":
        GC -= 1
    if s[j] == "G" or s[j] == "C":
        GC += 1
    if GC > GC_MAX:
        GC_MAX = GC
        max_i = i

print(s[max_i:max_i+N])
