import re

phoneNumRegex = re.compile(r'(\d{3}\.?\d{3}\.?\d{4})|(\d{3}-?\d{3}-?\d{4})')

# Alternate \d{3}([.-]?)\d{3}(\1)?\d{4}
match = phoneNumRegex.findall('My phone number is 983-332-3432 1-232-2323  1234567890  777.888.9999')

print('Phone Number Found: ' + str(match))

heroRegex =re.compile(r'Bat(man|mobile|copter|gun|underwear|wheel)')

str = 'Batman has a Batmobile that lost its Batwheel'
mo = heroRegex.search(str)
print(mo.group())

mo1 = heroRegex.findall(str)
print(mo1)

"""
# . will accept even new line and ignorecase

newlineRegex = re.compile('.*', re.DOTALL| re.I)
mo2 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo2.group())

# Substituting substring with sub()

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
>>'CENSORED gave the secret documents to CENSORED.'


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
"""

