'''
Source: https://leetcode.com/problemset/all/ 

Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

string = 'abcabcdbb'
array = list(string)

print(array)

subs = []
for i in range(len(array)-1):
    sub = []
    for letter in array:
        if letter in sub:
            array.pop(0)
            s = ''
            subs.append(s.join(sub))
            break
        else:
            sub.append(letter)
            print(sub)
print(subs)
print(max(subs,key=len))



