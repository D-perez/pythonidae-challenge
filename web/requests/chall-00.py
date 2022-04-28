#
### Challenge 00
#
#Send a GET request to URL and get the value of specific key on the response JSON.
#
#Get the value of `token`.
#
#Note: this is web service API, so you won't see a visual display.
#
### Test
#
#Access URL
#
#```
#https://pythonidae.herokuapp.com/web/generate
#```


import requests 

r = requests.get('https://pythonidae.herokuapp.com/web/generate')
print(f'The token is: {r.json()["token"]}')
