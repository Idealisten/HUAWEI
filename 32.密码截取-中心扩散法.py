password = input()
longest = 0


def extend_from_center(passwd, left, right):
    global longest
    while left >= 0 and right < len(passwd) and passwd[left] == passwd[right]:
        left -= 1
        right += 1
    if right - left - 1 > longest:
        longest = right - left - 1


for i in range(0, len(password)):
    extend_from_center(password, i, i)
    extend_from_center(password, i, i+1)

print(longest)


