'''
    A D F G V X
A | p h 0 q g 6
D | 4 m e a 1 y
F | l 2 n o f d
G | x k r 3 c v
V | s 5 z w 7 b
X | j 9 u t i 8

'''
indexes_of_letters = {
'0':'A',
'1':'D',
'2':'F',
'3':'G',
'4':'V',
'5':'X'
}

# getting lazy so hard coded grid
grid = [
['p','h','0','q','g','6'],
['4','m','e','a','1','y'],
['l','2','n','o','f','d'],
['x','k','r','3','c','v'],
['s','5','z','w','7','b'],
['j','9','u','t','i','8']]


clear_text = 'test'
enciphered_text = '' 

for letter in clear_text:
    for i in range(6): # number of columns and rows in the grid
        if letter in grid[i]:
            # take the row and column of the clear text letter 
            # and find the letters using the index dict
            enciphered_text += indexes_of_letters[str(i)]+indexes_of_letters[str(grid[i].index(letter))]

print(enciphered_text)