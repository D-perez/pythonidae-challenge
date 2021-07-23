import sys

clear_text = sys.argv[1]


# Solution

# creating alphabet then using translate
alphabet = 'abcedfghijklmnopqrstuvwxyz'
table = str.maketrans(alphabet, alphabet[::-1])

print(clear_text.translate(table))

