import sys

clear_text = sys.argv[1]

# Shared between solutions

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Solution 1

# 

rotated_text = ''

for i in range(len(clear_text)):
    if clear_text[i] in alphabet:
            rotated_text += alphabet[(alphabet.index(clear_text[i]) + 13 ) % 26]

print( 'solution 1: ' + rotated_text)


# Solution 2
# 

table = str.maketrans(alphabet, (alphabet[13:]+alphabet[0:13]))
print( 'solution 2: ' + clear_text.translate(table))
