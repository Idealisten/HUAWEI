n = int(input())
char_str_list = []
for i in range(n):
    char_str_list.append(input())

for i in range(n):
    beauty_list = [0] * 26
    for char in char_str_list[i]:
        beauty_list[ord(char)-97] += 1
    beauty_list.sort()
    beauty = 0
    for j in range(26):
        beauty += beauty_list[j]*(j+1)
    print(beauty)

