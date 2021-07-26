import os

files = os.scandir('.')

def scan(path='.'):
    files = os.scandir(path)
    for file in files:
        if 'README' in file.path:
            continue
        print(file.name)
        if file.is_dir():
            scan(file.path)
        # elif file.name[-3:] == '.md':
        #     print('the md path is' + file.path)
        #     os.system(f'touch {file.path[:-2]}py')
scan()



