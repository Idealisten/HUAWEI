import re


def check_password():
    password = input()

    if len(password) <= 8:
        return False

    digit = r"[0-9]"
    upper = r"[A-Z]"
    lower = r"[a-z]"
    chars = r"[^0-9a-zA-Z]"
    type_ = 0
    patterns = [digit, upper, lower, chars]
    for pattern in patterns:
        pw = re.search(pattern, password)
        if pw:
            type_ += 1
    if type_ < 3:
        return False

    for i in range(0, len(password)-3):
        if len(password.split(password[i:i+3])) >= 3:
            return False

    return True


if check_password():
    print("OK")
else:
    print("NG")
