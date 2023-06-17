import json

mnemonics = dict()

with open("morse_mnemonics.json", 'r') as json_file:
    mnemonics = json.load(json_file)


def get_letter_from_morse(morse : str):
    for key, value in mnemonics.items():
         if morse == value:
             return key
    raise Exception()
    

if __name__ == "__main__":

    option = 0
    while(True):
        option = input("Do you want to convert \n1. Morse to Text\n2. Text to Morse\n")
        option = int(option)
        if(option == 1 or option == 2):
            break

        print("Wrong option try again")

    if(option == 1):
        morse_key_list = list(mnemonics.values())
        while True:

            morse_code = input("Write Your Morse code :\n")

            morse_code_list = morse_code.split(" ")
            text_to_print = ""
            try:
                for each_code in morse_code_list:
                    text_to_print += get_letter_from_morse(each_code)

                print(text_to_print)
                break
            except Exception as identifier:
                print("your morse code has some error\nTry again")

    if(option == 2):
        
            
        text_to_convert = input("Write your text :\n")
        
        for letter in text_to_convert:
            print(str(mnemonics[letter.upper()]), end=" ")