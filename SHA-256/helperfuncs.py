from baseoperations import ADD, AND, OR, XOR, LOTR, ROTR, SHR, SHL

N = 32

def get_binary(number, len = 32):
    return str(f"{number:0b}").zfill(len)

def small_sigma_0(num):
    return ROTR(num, 7) ^ ROTR(num, 18) ^ SHR(num, 3)

def small_sigma_1(num):
    return ROTR(num, 17) ^ ROTR(num, 19) ^ SHR(num, 10)

def capital_sigma_0(num):
    return ROTR(num, 2) ^ ROTR(num, 13) ^ ROTR(num, 22)

def capital_sigma_1(num):
    return ROTR(num, 6) ^ ROTR(num, 11) ^ ROTR(num, 25)

def choice(i1, i2, i3):
    return_str = ""
    i1b = get_binary(i1)
    i2b = get_binary(i2)
    i3b = get_binary(i3)
    for i,c in enumerate(i1b):
        return_str += i2b[i] if c == "0" else i3b[i]

    return return_str

def majority(i1, i2, i3):
    return_str = ""
    i1b = get_binary(i1)
    i2b = get_binary(i2)
    i3b = get_binary(i3)

    for a, b, c in zip(i1b, i2b, i3b):
        return_str += a if a == b else c
    
    return return_str

def dec_from_bin(bin_str):
    return int(bin_str, 2)