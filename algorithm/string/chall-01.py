# ## Challenge 01
# Given a string `U` and list of string `E`.
# Create a new list by concatenating each element of `E` with `U`.
# ## Test
# Given a string `U`
# ```
# https://pythonidae.herokuapp.com/
# ```
# and a list of string `E`
# ```
# web/generate
# web/identify
# web/cookies
# ```
# the result should be
# ```
# https://pythonidae.herokuapp.com/web/generate
# https://pythonidae.herokuapp.com/web/identify
# https://pythonidae.herokuapp.com/web/cookies
# ## Remarks
# Concatenation is used a lot, especially for generating target. 
# Enumerating directory is common tasks in recon where you have a base URL and some directories or files. For each request, you need to get a full URL which combining base URL and the endpoints.

U = 'https://pythonidae.herokuapp.com/'
E = ['web/generate','web/identify','web/cookies']

################ In place list change
# print(list(map( lambda x: U+x,E) ) )

################ new list w/ concat
res = []
for extension in E:
    res.append(U + extension)

print(res)