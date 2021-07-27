import requests

domain = "https://stackoverflow.com/"
wordlist = ['random','company','company/careers','teams']

for word in wordlist:
    try:
        r = requests.head(domain + word)
        print(str(r.status_code) + ': ' + domain + word)
        # prints the int of the status code. Find more at httpstatusrappers.com :)
    except requests.ConnectionError:
        print("failed to connect")

