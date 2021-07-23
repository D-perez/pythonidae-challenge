
'''
   0 1 2 3 4 5 6 7 8 9 0
0  h . . . o . . . r . .
1  . e . l . _ . o . l .
2  . . l . . . w . . . d

hello world
horel ollwd
'''

import sys

rows = int(sys.argv[2])
string = sys.argv[1]
string = string.replace(' ','_') # this saves spaces in the string so they are not deleted later
cipher_text = []
grid = []


for i in range(rows):
    grid.append([])
    for o in range(len(string)):
        grid[i].append(' ')

descend = True
row = 0

for i in range(len(string)):
  grid[row][i]=string[i]
  if row==0: # if you are at the top row or the roof flag set flag to descend
    descend = True
  elif row==rows-1: # creates zig zag 
    descend = False
  if descend:
    row+=1 
  else:
    row-=1


for i in range(rows):
    for o in range(len(string)):
        if grid[i][o] != ' ':
            cipher_text.append(grid[i][o])

for i in range(rows):
    print(''.join(grid[i]))
print( ''.join(cipher_text).replace('_', ' ') )

