from operations import small_sigma_0, small_sigma_1, capital_sigma_0, capital_sigma_1, get_binary, choice, majority
from operations import ADD, AND, OR, XOR
from constants import get_constants
from typing import List
import math
from pwn import xor

CHUNK = 512


def get_unpadded_binary(string:str) -> str:
    unpadded_binary = ""
    for char in string:
        unpadded_binary += bin(ord(char))[2:].zfill(8)
    return unpadded_binary


def get_padded_chunks(string:str) -> List[str]:
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

def get_words(chunk:str):
    
    words = list(map(''.join, zip(*[iter(chunk)]*32)))
    # print(f"{words=}")
    # [print(word) for word in words]
    for i in range(48):
        term_1 = small_sigma_1(words[16 + i - 2])
        term_2 = words[16 + i - 7]
        term_3 = small_sigma_0(words[16 + i - 15])
        term_4 = words[16 + i - 16]
        new_word = ADD(term_1 , term_2, term_3, term_4)
        print(f"{new_word}")
        words.append(new_word)
        

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

    unpadded_bin = get_unpadded_binary(string_to_hash)
    # print(f"{unpadded_bin=}")

    padded_chunk = get_padded_chunks(unpadded_bin)
    # print(f"{padded_chunk=}")

    init_hash_val = get_init_hash_values()

    for index, chunk in enumerate(padded_chunk):

        words = get_words(chunk)
        # print()
        # [print(word) for word in words]
        for word in words:
            T1 = capital_sigma_1(
                init_hash_val['e']
            ) + choice(
                init_hash_val['e'],
                init_hash_val['f'],
                init_hash_val['g']
            )
            pass
        
        print(f"{init_hash_val=}")

        # Compression


    





if __name__ == '__main__':
    main()

