'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

input = ['flower','flame','flore']
#input = ['cat','dog','guano']

def LongestPrefix(input):
    final_pos = -1
    item = input[0]
    position = 0
    for letter in item:
        if  input[1][position] == letter and input[2][position] == letter:
            position += 1
            final_pos = position
            pass
        else:
            break
    if final_pos == -1:
        prefix = ''
    else:
        prefix = item[:position]
    return prefix
print(LongestPrefix(input))