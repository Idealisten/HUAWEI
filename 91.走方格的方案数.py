# 递归

n, m = map(int, input().split())


def steps_of_square(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0 or b == 0:
        return 1
    else:
        return steps_of_square(a, b - 1) + steps_of_square(a - 1, b)


print(steps_of_square(n, m))
