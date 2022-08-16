# 十进制与二进制的转换、map函数、join函数
ip = input()
ip2 = input()


def dec_to_bin(dec):
    bin_list = []
    dec = int(dec)
    while dec//2 != 0:
        bin_list.append(str(dec % 2))
        dec = dec // 2
    bin_list.append(str(dec % 2))
    if len(bin_list) < 8:
        for j in range(8-len(bin_list)):
            bin_list.append("0")
    bin_list.reverse()
    return "".join(bin_list)


def bin_to_dec(bin):
    dec = 0
    for k in range(len(bin)):
        dec += int(bin[len(bin)-k-1])*pow(2, k)
    return str(dec)


ip2_bin = dec_to_bin(ip2)
if len(ip2_bin) < 32:
    ip2_bin = "0"*(32-len(ip2_bin)) + ip2_bin
sub_ip_1 = ip2_bin[0:8]
sub_ip_2 = ip2_bin[8:16]
sub_ip_3 = ip2_bin[16:24]
sub_ip_4 = ip2_bin[24:32]
sub_ip_list = [sub_ip_1, sub_ip_2, sub_ip_3, sub_ip_4]
ip2_dec = ".".join(map(bin_to_dec, sub_ip_list))

ip_bin = "".join(map(dec_to_bin, ip.split(".")))

ip_dec = 0
for i in range(len(ip_bin)):
    ip_dec += int(ip_bin[len(ip_bin)-i-1])*pow(2, i)
print(ip_dec)
print(ip2_dec)


