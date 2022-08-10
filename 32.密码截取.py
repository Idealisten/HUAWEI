# 暴力搜索
password = input()
password2 = ""
for p in password:
    if p.isdigit() is True or p.isalpha() is True:
        password2 += p
max_reg = 0
tem_reg = 0
reg = 1
for i in range(len(password2)):
    for j in range(i+1, len(password2)+1):
        reg = 1
        sub_password = password2[i:j]
        if sub_password == "":
            continue
        if len(sub_password) == 1:
            tem_reg = 1
            continue
        else:
            tem_reg = len(sub_password)
            for k in range(int(len(sub_password)/2)):
                if sub_password[k] != sub_password[len(sub_password) - k - 1]:
                    reg = 0
                    break
        if reg == 1:
            if tem_reg > max_reg:
                max_reg = tem_reg
print(max_reg)
