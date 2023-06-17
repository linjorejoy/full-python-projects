import math

primes =  [ 2,   3,   5,   7,   11,  13,  17,  19,
            23,  29,  31,  37,  41,  43,  47,  53,
            59,  61,  67,  71,  73,  79,  83,  89,
            97,  101, 103, 107, 109, 113, 127, 131,
            137, 139, 149, 151, 157, 163, 167, 173,
            179, 181, 191, 193, 197, 199, 211, 223,
            227, 229, 233, 239, 241, 251, 257, 263,
            269, 271, 277, 281, 283, 293, 307, 311]



def get_constants():
    hexs = []
    constants = []

    for prime in primes:
        cube_root = prime ** (1/3)
        decimal_part = cube_root -  math.floor(cube_root)

        hex_str = ""

        for _ in range(8):
            product = decimal_part * 16
            int_part = math.floor(product)
            hex_str += f"{int_part:x}"
            decimal_part = product - int_part

        hexs.append(hex_str)
        binary_value = str(bin(int(hex_str, base=16))[2:]).zfill(32)
        constants.append(binary_value)
    
    return constants
