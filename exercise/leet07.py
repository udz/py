'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
'''
question = '[{()}]()())'
compare = []
result = True

for symbol in question:
    if symbol in ('[','{','('):
        compare.append(symbol)
    if symbol == ']':
        if compare.pop() != '[':
            result = False
            break
    if symbol == '}':
        if compare.pop() != '{':
            result = False
            break
    if symbol == ')':
        if compare.pop() != '(':
            result = False
            break

if len(compare) > 0:
    result = False

print(result)