import sys

clear_text = sys.argv[1]

# Shared between solutions

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Solution 1

# Uses a for loop and modulo to shift the index of the letter in the alphabet by 13.

rotated_text = ''

for i in range(len(clear_text)):
    if clear_text[i] in alphabet:
            rotated_text += alphabet[(alphabet.index(clear_text[i]) + 13 ) % 26]

print( 'solution 1: ' + rotated_text)


# Solution 2

# Uses a table to translate the a-z alphabet to n-za-m 


table = str.maketrans(alphabet, (alphabet[13:]+alphabet[0:13]))
print( 'solution 2: ' + clear_text.translate(table))
