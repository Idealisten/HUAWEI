# 递归
m, n = map(int, input().split())


def func(a, b):
    # 0个或1个苹果，1个盘子
    if a == 0 or a == 1 or b == 1:
        return 1
    # 盘子数量大于苹果，多余的盘子并不影响结果，可以简化为func(a,a)
    elif b > a:
        return func(a, a)
    # 苹果数量大于等于盘子，分两种情况
    # 1.至少有一个盘子不放苹果
    # 在计算有一个盘子不放苹果func(a, b-1)的时候会递归计算func(a,b-2)直到b=1，计算b-1个盘子时已经递归包含了b-1个盘子的情况
    # 2.每个盘子都有至少一个苹果，相当于将问题化简为将a-b个苹果放到b个盘子里
    else:
        return func(a, b-1) + func(a-b, b)


print(func(m, n))
