#!
# pw.py - An insecure password locker program

passwords = {'gmail':'password1',
             'outlook':'p@ssword',
             'trello':'trem232'}

import sys
import pyperclip

if len(sys.argv)<2:
    print('Usage: python pwlocker.py [account]  - copy account password')
    sys.exit()


account = sys.argv[1] # Assign first argument in the account variable

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for '+account+ ' copied to clipboard')
else:
    print('There\'s no password saved for '+account)
