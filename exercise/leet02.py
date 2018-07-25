# Given a 32-bit signed integer, reverse digits of an integer.
# Input: -123
# Output: -321

input = -12340
sign = 'positive'
if input < 0:
    sign = 'negative'
    input = abs(input)
temp1 = str(input)
output = int(temp1[::-1])

if sign == 'negative':
    output = -output
print(output)
