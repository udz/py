'''
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

phone = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
numbers = '24'
#numbers = int(input('Please enter numbers of which to find letter combination'))
temp = []
for digit in numbers:
    temp.append(phone[int(digit)])

temp2 = []
for letter1 in temp[0]:
    for letter2 in temp[1]:
        temp2.append(str(letter1 + letter2))

print(temp2)