from helperfuncs import get_binary, small_sigma_0, small_sigma_1, capital_sigma_0, capital_sigma_1, choice, majority, dec_from_bin
from baseoperations import ADD, AND, OR, XOR, LOTR, ROTR, SHR, SHL
from constants import get_constants
N= 32


words = ["01100001011000100110001100000000",
"00000000000011110000000000000000",
"01111101111110000110010000000101",
"01100000000000000000001111000110",
"00111110100111010110111101011010",
"00000001100000111111110000000000",
"00011010010010011111111111011110",
"11100010111000101100001100001110",
"11000000001000010101110000010010",
"10110111110101100111100110100010",
"11100101101110110011010000001001",
"00110010011001100110011111101001",
"11111110010000001001110010100111",
"00011001010011110010011011000100",
"01110000111000010101001111100000",
"11001100000011001100100101101111",
"01011100110010101110100011011101",
"11111111101110001111001111110100",
"01011001111100101001101110110011",
"10101110011100111100011100010110",
"01110101110110011100100110010111",
"11001110001100011001100001111100",
"01110101100101010001000011010001",
"10101001001100001111011111010101",
"10111000010010000000111101110100",
"00111001100000011010110001011111",
"11101000011111000010000011111000",
"00000011000001111011101001011000",
"10100011011101100010100000100010",
"01010011010100011110110010000101",
"11011111100100101001011111010000",
"01011011001100110101000010010100",
"01111010011001110111011001010001",
"01110101111001001101111101010100",
"01111100010011011001011010011101",
"10011000011111010001010010001000",
"11001000111100110001110010011001",
"10111111001001010100011000011110",
"01000010001101110101100001011110",
"00101101001000000110111100101111",
"01000111101101100100110000000110",
"11010101001010011100010001101100",
"11001111011111000011010100111100",
"10000001101010100001001010111010",
"01111010100100110101101000111001",
"00000000011011001111111101111000",
"11001010111011010101100001001011",
"1"*32]


# word = '11000011000110000011111111111111'

for word in words:
    word_int = int(word, 2)

    # print("\n\nlower sigma 0")
    ROTR7 = ROTR(word_int, 7)
    ROTR18 = ROTR(word_int, 18)
    SHR3 = SHR(word_int, 3)

    # print(get_binary(ROTR7))
    # print(get_binary(ROTR18))
    # print(get_binary(SHR3))
    # print("-"*32)
    # print(get_binary(ROTR7 ^ ROTR18 ^ SHR3))
    # print(get_binary(small_sigma_0(word_int)))
    print(get_binary(ROTR7 ^ ROTR18 ^ SHR3) == get_binary(small_sigma_0(word_int)))

    # print("\n\nlower sigma 1")
    ROTR17 = ROTR(word_int, 17)
    ROTR19 = ROTR(word_int, 19)
    SHR10 = SHR(word_int, 10)

    # print(get_binary(ROTR17))
    # print(get_binary(ROTR19))
    # print(get_binary(SHR10))
    # print("-"*32)
    # print(get_binary(ROTR17 ^ ROTR19 ^ SHR10))
    # print(get_binary(small_sigma_1(word_int)))
    print(get_binary(ROTR17 ^ ROTR19 ^ SHR10) == get_binary(small_sigma_1(word_int)))

# print(ADD(2**32 - 1,2**32 - 1,2**32 - 1))

# word = '01100001011000100110001100000000'
# num = int(word,2)
# num1 = ROTR(num, 1)
# num10 = ROTR(num, 10)
# num20 = ROTR(num, 20)
# num30 = ROTR(num, 30)
# num32 = ROTR(num, 32)
# num64 = ROTR(num, 64)
# num512 = ROTR(num, 512)
# print("num1 : ", num1)
# print("num10 : ", num10)
# print("num20 : ", num20)
# print("num30 : ", num30)
# print("num32 : ", num32)
# print("num64 : ", num64)
# print("num512 : ", num512)
# print(f"num    : {num:>20} : {get_binary(num):>32}")
# print(f"num1   : {num1:>20} : {get_binary(num1):>32}")
# print(f"num10  : {num10:>20} : {get_binary(num10):>32}")
# print(f"num20  : {num20:>20} : {get_binary(num20):>32}")
# print(f"num30  : {num30:>20} : {get_binary(num30):>32}")
# print(f"num32  : {num32:>20} : {get_binary(num32):>32}")
# print(f"num64  : {num64:>20} : {get_binary(num64):>32}")
# print(f"num512 : {num512:>20} : {get_binary(num512):>32}")

# print(len(word))

# print(int(word, 2))

# print(LOTR(5,1))
# print("0b",word, sep="")
# print(bin(small_sigma_0(int(word, 2))))


# str1 = "adadsvgvsdvsdvsdvdvsdv"

# print(str1)
# print(str1[:5])
# print(str1[5:])

# print(bin(ord('a'))[2:].zfill(8))

# print(hex_to_binary(0xf28a2f98))



# print(bin(int('f28a2f98', 16)))
# print(len('1000010100010100010111110011000'))
# a = f"{15:x}"
# print(a)
# print(hex(8))
# print(hex(10))
# print(hex(15))

# print([ch for ch in get_binary(2)])
# print(get_binary(32)[0])
# print(get_binary(32)[1])
# print(get_binary(32)[2])
# print(get_binary(1)[31])

# print(get_binary(1500))
# print(get_binary(250))
# print("-"*32)
# print(get_binary(XOR(1500, 250)))

# print(get_binary_2(5))
# print(get_binary_2(10))

# print(get_binary(1500))
# print(get_binary(LOTR(1500,10, 32)))
# print(get_binary(LOTR(1500,20, 32)))
# print(get_binary(LOTR(1500,30, 32)))

# print(leftRotate(1500,10))
# print(leftRotate(1500,20))
# print(leftRotate(1500,30))
# print(2**32)
# print(get_binary(20))
# print(get_binary(40))


# print(get_binary_2(5<<1))

# print("{0:32b}".format(37))
# print("{0:32b}".format(37>>1))
# print("{0:32b}".format(37<<1))
# character = "5"

# print(f"{5:32b}".zfill(32))
# print(f"{10:32b}".zfill(32))
# print(f"{37>>1:32b}".zfill(32))
# print(f"{37<<1:32b}".zfill(32))

# print("50".zfill(10))

# c = 55
# print(c)
# print(c>>1)
# print(c<<2)

# print(get_binary(c))
# new_c = c <<  1
# print(get_binary(new_c))



# print(bytes("a",'utf-8'))

# def DecimalToBinary(num):
#     if num >= 1:
#         DecimalToBinary(num // 2)
#         print (num % 2 )

# DecimalToBinary(9600)

