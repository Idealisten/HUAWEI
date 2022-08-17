key = input()
bf_encryption = input()
key = key.lower()
key_list = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_list = list(alphabet)
for a in key:
    if a not in key_list:
        key_list.append(a)
if len(key_list) < 26:
    for k in key_list:
        alphabet_list.remove(k)
key_list.extend(alphabet_list)
new_alphabet = "".join(key_list)
# print(new_alphabet)

af_encryption = ""
for b in bf_encryption:
    x = alphabet.index(b)
    af_encryption += new_alphabet[x]
print(af_encryption)


