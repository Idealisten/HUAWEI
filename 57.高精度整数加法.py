"""
分别将两个操作数a，b从左到右入栈，再从栈顶依次pop，达到先计算低位的目的
每次分别将两个操作数的当前位与进位标志相加求余得到结果c的当前位并入结果c栈
同时计算下一位的标志位
最终两运算数栈都为空时检查标志位，如果为1需要在结果栈中再入1
"""
a = input()
b = input()
c = ""
stack_a = []
stack_b = []
stack_c = []
flag = 0

for i in range(len(a)):
    stack_a.append(a[i])
for i in range(len(b)):
    stack_b.append(b[i])

while stack_a and stack_b:
    ta = int(stack_a.pop())
    tb = int(stack_b.pop())
    tc = (ta + tb + flag) % 10
    stack_c.append(str(tc))
    if ta + tb + flag >= 10:
        flag = 1
    else:
        flag = 0


if len(stack_b) == 0:
    while stack_a:
        ta = int(stack_a.pop())
        tc = (ta + flag) % 10
        stack_c.append(str(tc))
        if ta + flag >= 10:
            flag = 1
        else:
            flag = 0
elif len(stack_a) == 0:
    while stack_b:
        tb = int(stack_b.pop())
        tc = (tb + flag) % 10
        stack_c.append(str(tc))
        if tb + flag >= 10:
            flag = 1
        else:
            flag = 0
if flag == 1:
    stack_c.append("1")

while stack_c:
    c = c + stack_c.pop()

print(c)