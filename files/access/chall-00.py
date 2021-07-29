import os
import sys

# solution 1

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


# solution 2

list_dirs_switch = True if len(sys.argv) > 1 and sys.argv[1] == 'list-dirs' else False


contents = os.scandir('.')

for content in contents:
    if content.is_dir() and list_dirs_switch:
        print(content.name + '/')
    else:
        print(content.name)
