print('This\'s a\n \ttest')
print(r'This\'s a test') # for raw output

#Multiline text
print('''Dear Sir,

I came to know about the latest update you shared via email earlier this week from Dinesh.

Regards,
Ujjwal''')

""" This is
a multi line
comment
"""

print('---end---')

text = 'Testing Testing what are you testing?'

# slicing
print(text[0:5])
print(text)

# itirate individual characters in a string
for char in text:
    print(char)

print(text.upper())

print(text.encode(encoding='utf-8',errors='strict'))

print(text.swapcase())

# validate case insensitive
feeling = input('How are you feeling?')
if feeling.lower() == 'great':
    print('Me too')
else:
    print('Have a good day')

print(text.lower().islower())

# substring in string
if 'Hello' in 'Hello World!':
    print('Hello')
else:
    print('Oops!')

# startswith() endswith()
if text.startswith('Test'):
    print('Text starts with "Test"')
if text.endswith('ing'):
    print('Text ends with "ing"')

# Validation
while True:
    password = input('Please enter password of your choice: ')
    if password.isalnum():
        break
    print('Try Entering Alpha Numeric Password')

# join() and split()
text1 = text.split()
print(text1)
print(', '.join(text1))

# split in the occurance of substring in the string and join
splitted = 'MyABCnameABCisABCSimon'.split('ABC')
print(splitted)
print(' '.join(splitted))


# justify - rjust(), ljust(), center()
print('Ujjwal'.rjust(20,'*'))
print('Ujjwal'.rjust(20))

print('Ujjwal'.ljust(20,'-'))
print('Ujjwal'.center(20,'-'))

# strip() from the ends of the text
# Typically used to take out white spaces in the text
print(text.strip('Tg?'))

# Regardless of the order 'ting?' gets removed from the right
print(text.rstrip('gi?tn'))



