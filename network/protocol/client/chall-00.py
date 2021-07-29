import requests
import sys

domain = sys.argv[1]
wordlist_arg = sys.argv[2]

wordlist = open(wordlist_arg,'r').readlines()

for word in wordlist:
    try:
        r = requests.head(domain + word[:-1]) # gets rid of \n

        print(str(r.status_code) + ': ' + domain + word)
        # prints the int of the status code. Find more at httpstatusrappers.com :)
    except requests.ConnectionError:
        print("failed to connect")
