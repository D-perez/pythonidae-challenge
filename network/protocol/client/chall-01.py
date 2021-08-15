import sys

ip = sys.argv[1] if len(sys.argv) > 1 else '10.10.10.10' 
with open('user.txt','r') as user_list:
    users = [user.strip('\n') for user in user_list.readlines()]
with open('passwords.txt','r') as passwords_list:
    passwords = [passes.strip('\n') for passes in passwords_list.readlines()]

print(users)
print(passwords)