# Encoder / Decoder

import base64

def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

"""
# Following is equivalent to above function
def stringToBase64(s):
    b = bytes(s, 'utf-8')
    return base64.b64encode(b)
"""

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')

encoded = stringToBase64('Test')
print(encoded)
decoded = base64ToString(encoded)
print(decoded)
