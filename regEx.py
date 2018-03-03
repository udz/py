
# Reg Ex example

# https://docs.python.org/3/howto/regex.html

# match() search() findall() finditer()

import re

'''
Compilation flags
A - ASCII, performs ASCII only matching instead of full Unicode matching
I - IGNORECASE, [A-Z] matches both cases
S - DOTALL,  '.' will match everything including a new line
M - MULTILINE, ^ and $ matches beginning and end of new line instead of just beginning and end
L - LOCALE,
X - VERBOSE
'''
re.A | re.I

testText = "an4 ball Fell Out of the window udshrestha@gmail.com xyz@test.com"
result = []

p = re.compile(r'[a-z]+')

# match()
# methods of match object
# group() start() end() span()
match = p.match(testText)
print(match)
print(match.group())  # This only returns the first instance of matched item
print(match.span())

search = p.search(testText)
print(search)

# findall()
# Returns all the instances of the matched items in a list format
print('\n*******findall() Function*********\n')
result = p.findall(testText)
print(result)

# finditer()
# goes through one by one
print('\n*******finditir() Function*********\n')
iterator = p.finditer(testText)
for match in iterator:
    print(match.group())

# Module Level Functions

print('\n*******Module Level Function*********\n')
print(re.findall(r'\w+',testText))
