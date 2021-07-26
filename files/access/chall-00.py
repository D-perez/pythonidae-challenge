import os
import sys


your_path = sys.argv[1] if len(sys.argv) > 1 else '.'
files = os.scandir(your_path)




for file in files:
    name = file.name
    if len(name) > 17:
        name = name[:17] + '...'
    while len(name) < 20:
        name += ' '
    if file.is_dir():
        name += ' directory' 
    else:
        name += ' file' 
    print(name)



