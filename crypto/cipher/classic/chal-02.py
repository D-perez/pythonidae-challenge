import sys

# Solution

a = int(sys.argv[1])
b = int(sys.argv[2])
input_string = sys.argv[3]


# encrypt

# print(a,b,clear_text)

def encrypt():
    encrypted_text = ''
    for letter in input_string:
        if letter == ' ':
            encrypted_text += ' '
            continue
        p = ord(letter) - 97 # p stands for position
        encrypted_text += chr((a*p+b)% 26 + 97)
    print(input_string,'\n',encrypted_text)
# decrypt



def decrypt():
    decrypted_text = ''
    for letter in input_string:
        if letter == ' ':
            decrypted_text += ' '
            continue
        p = ord(letter) - 97 # p stands for position
        print(p)
        print(a**(-1))
        decrypted_text += chr(int(((pow(a,-1,26)) * (p - b)) % 26 + 97))
    print(decrypted_text)

decrypt()