import json


morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]


alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

mnemonics = dict()

for letter, morse_code in zip(alphabets, morse):
    mnemonics[letter] = morse_code
    

with open("morse_mnemonics.json", 'w') as json_file:
    json.dump(mnemonics, json_file, indent=2)