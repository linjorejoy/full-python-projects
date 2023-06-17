from helperfuncs import get_binary, small_sigma_0, small_sigma_1, capital_sigma_0, capital_sigma_1, choice, majority, dec_from_bin
from baseoperations import ADD, AND, OR, XOR, LOTR, ROTR, SHR, SHL
from constants import get_constants
import math

CHUNK = 512


def get_unpadded_binary(string):
    unpadded_binary = ""
    for char in string:
        unpadded_binary += bin(ord(char))[2:].zfill(8)
    return unpadded_binary


def get_padded_chunks(string):
    chunks = []
    total_length = len(string)
    while len(string) > CHUNK:
        chunks.append(string[:512])
        string = string[512:]

    # print(f"To be padded : {len(string)}")
    length_rem = len(string)
    string = string + "0"*(448 - length_rem) + get_binary(total_length, len=64)
    chunks.append(string)

    return chunks

def get_words(chunk):
    words = list(map(''.join, zip(*[iter(chunk)]*32)))
    for i in range(48):
        term_1 = small_sigma_1(int(words[16 + i - 2], 2))
        term_2 = int(words[16 + i - 7], 2)
        term_3 = small_sigma_0(int(words[16 + i - 15], 2))
        term_4 = int(words[16 + i - 16], 2)
        new_word_int = ADD(term_1 + term_2 + term_3 + term_4)

        words.append(get_binary(new_word_int))
        
    return words

def get_init_hash_values():
    primes = {"a":2,"b":3,"c":5,"d":7,"e":11,"f":13,"g":17,"h":19}
    # primes = [2,3,5,7,11,13,17,19]
    for key in primes.keys():
        root = primes[key] ** (1/2)
        int_part = math.floor(root)
        fr_part = root - int_part
        new_int = fr_part * 2**32
        primes[key] = get_binary(int(new_int))

    return primes

def get_temporary_words():
    
    pass


def main():
    # string_to_hash = input("What is the Chars : ")
    string_to_hash = 'abc'
    constants = get_constants()
    # print(constants)

    unpadded_bin = get_unpadded_binary(string_to_hash)

    init_hash_val = get_init_hash_values()

    for index, chunk in enumerate(get_padded_chunks(unpadded_bin)):

        words = get_words(chunk)
        for word in words:
            T1 = capital_sigma_1(
                int(init_hash_val['e'], 2)
            ) + choice(
                int(init_hash_val['e'], 2),
                int(init_hash_val['f'], 2),
                int(init_hash_val['g'], 2)
            )
            pass
        
        print(init_hash_val)

        # Compression


    





if __name__ == '__main__':
    main()


        # words = list(map(''.join, zip(*[iter(chunk)]*32)))

        # [print(word) for word in words]
        # print("\n"*3)
        # for i in range(48):
            # print(f"\n\n{15 + i + 1 - 2} + {15 + i + 1 - 7} + {15 + i + 1 - 15} + {15 + i + 1 - 16}\nW{i + 16}")
            # term_1 = small_sigma_1(int(words[16 + i - 2], 2))
            # term_2 = int(words[16 + i - 7], 2)
            # term_3 = small_sigma_0(int(words[16 + i - 15], 2))
            # term_4 = int(words[16 + i - 16], 2)
            # new_word_int = ADD(term_1 + term_2 + term_3 + term_4)
            # print(f"W{16 + i - 16:4} {words[16 + i - 16]} ->    {get_binary(term_4)} +")
            # print(f"W{16 + i - 15:4} {words[16 + i - 15]} -> s0 {get_binary(term_3)} +")
            # print(f"W{16 + i - 7:4} {words[16 + i - 7]} ->    {get_binary(term_2)} +")
            # print(f"W{16 + i - 2:4} {words[16 + i - 2]} -> s1 {get_binary(term_1)} +")
            # print("-"*34)
            # print(f"{get_binary(new_word_int)}")
            # print(f"W{i + 16} \n  {get_binary(term_4)} +\n  {get_binary(term_3)} +\n  {get_binary(term_2)} +\n  {get_binary(term_1)} \n{('-'*34)}\n= {get_binary(new_word_int)} ")

        #     words.append(get_binary(new_word_int))

        # [print(f"W{i}", word) for i, word in enumerate(words)]
        # print(len(words))
        # print(len(chunk), ":", chunk)


    # print(len('chunk_in_get_padded_chunks'*10))

    


    # print(unpadded_bin)