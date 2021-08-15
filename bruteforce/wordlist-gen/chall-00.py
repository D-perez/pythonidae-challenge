# # recursion bruteforce
# wordlist = []
# def brute(string, length, charset):
#     if len(string) == length:
#         return 0
#     for char in charset:
#         temp = string + char
#         if len(temp) >= length: wordlist.append(temp)
#         brute(temp, length, charset)

# brute('', 3, 'abcdefghijklmnopqrstuvwxyz')

# print(wordlist)


# itertools brute force

