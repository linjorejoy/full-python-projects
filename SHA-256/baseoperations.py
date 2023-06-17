
N = 32
TWO_P_N = 2**32

def ADD(*nums):
    total = 0
    for num in nums:
        total += num
        total = total % TWO_P_N
    return total

def AND(N1, N2):
    return N1 & N2

def OR(N1, N2):
    return N1 | N2

def XOR(N1, N2):
    return N1 ^ N2

def LOTR(n, d):
    d = d % N
    return ((n << d) % (1 << N)) | (n >> (N - d))
    
def ROTR(n, d):
    d = d % N
    return LOTR(n, N-d)

def SHR(b, shift):
    return b >> shift

def SHL(b, shift):
    return b << shift

