import os
import sys

your_path = sys.argv[1]
files = os.listdir(your_path)
keyword = 'your_keyword'


print(files)