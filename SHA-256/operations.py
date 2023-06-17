from functools import reduce
from pwn import xor
    
N = 32
TWO_P_N = 2**32


def get_binary(number, len = N):
    number = number % TWO_P_N
    return str(f"{number:0b}").zfill(len)


def ADD(*nums):
    total = 0
    for num in nums:
        total += int(num, 2)
        total = total % TWO_P_N
    return get_binary(total)

def AND(*nums):
    int_nums = [int(num, 2) for num in nums]
    return get_binary(reduce(lambda x, y: x & y, int_nums))

def OR(*nums):
    int_nums = [int(num, 2) for num in nums]
    return get_binary(reduce(lambda x, y: x | y, int_nums))

def XOR(*nums):
    int_nums = [int(num, 2) for num in nums]
    return get_binary(reduce(lambda x, y: x ^ y, int_nums))

def LOTR(n, d):
    n = int(n, 2)
    d = d % N
    return_num = ((n << d) % (1 << N)) | (n >> (N - d))
    return get_binary(return_num)
    
def ROTR(n, d):
    d = d % N
    return LOTR(n, N-d)

def SHR(b, shift):
    b = int(b, 2)
    return get_binary(b >> shift)

def SHL(b, shift):
    b = int(b, 2)
    return get_binary(b << shift)



def small_sigma_0(num: str) -> str:
    return XOR(ROTR(num, 7) , ROTR(num, 18) , SHR(num, 3))

def small_sigma_1(num: str) -> str:
    return XOR(ROTR(num, 17) , ROTR(num, 19) , SHR(num, 10))

def capital_sigma_0(num: str) -> str:
    return XOR(ROTR(num, 2) , ROTR(num, 13) , ROTR(num, 22))

def capital_sigma_1(num: str) -> str:
    return XOR(ROTR(num, 6) , ROTR(num, 11) , ROTR(num, 25))

def choice(i1:str, i2:str, i3:str) -> str:
    return_str = ""
    for i,c in enumerate(i1):
        return_str += i2[i] if c == "0" else i3[i]
    return return_str

def majority(i1: str, i2: str, i3: str) -> str:
    return_str = ""

    for a, b, c in zip(i1, i2, i3):
        return_str += a if a == b else c
    
    return return_str

def dec_from_bin(bin_str:str) -> int:
    return int(bin_str, 2)


