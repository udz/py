#! python3
# pnoneAndEmailFinder.py

# import pyperclip
import re

# Phone Finding RegEx
# phoneRegex = re.compile(r'\d{3}([ .-]?)\d{3}(\1)?\d{4}')

phoneRegex = re.compile(r'\d{3}[ .-]?\d{3}[ .-]?\d{4}')

# Email Finding RegEx
emailRegex = re.compile(r'[a-z]\w+?\.?\w+@\w{2,20}[.]\w{2,7}',re.I)

text = '''
    My phone number is 983-332-3432
    1-232-2323  1234567890  777.888.9999 
    udshrestha@gmail.com  xyz@hotmail.co ujjwal.shrestha@gmail.com
    '''


phones = phoneRegex.findall(text)
emails = emailRegex.findall(text)

print(phones)
print(emails)

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.

"""

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
"""
