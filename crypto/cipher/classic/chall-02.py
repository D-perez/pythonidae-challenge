import sys

# Solution

a = int(sys.argv[1])
b = int(sys.argv[2])
input_string = sys.argv[3]


# encrypt

# print(a,b,clear_text)

def encipher():
    enciphered_text = ''
    for letter in input_string:
        if letter == ' ':
            enciphered_text += ' '
            continue
        p = ord(letter) - 97 # p stands for position
        enciphered_text += chr((a*p+b)% 26 + 97)
    print(input_string,'\n',enciphered_text)

    
# decrypt



def decipher():
    deciphered_text = ''
    for letter in input_string:
        if letter == ' ':
            deciphered_text += ' '
            continue
        p = ord(letter) - 97 # p stands for position
        print(p)
        print(a**(-1))
        deciphered_text += chr(int(((pow(a,-1,26)) * (p - b)) % 26 + 97))
    print(deciphered_text)

decipher()