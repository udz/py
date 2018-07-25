'''
have the function AlphabetSoup(str) take the str string parameter being passed 
and return the string with the letters in alphabetical order (ie. hello becomes ehllo). 
Assume numbers and punctuation symbols will not be included in the string. 

Sample Test Cases

Input:"coderbyte"
Output:"bcdeeorty"

Input:"hooplah"
Output:"ahhloop"
'''

string = 'zMyohmyacd'

def AlphabetSoup(str):
    new_list = []
    sorted_string = ''
    for char in str:
        new_list.append(char)
    new_list.sort()
    #new_list.reverse()
    for letter in new_list:
        sorted_string += letter 
    return sorted_string

print(AlphabetSoup(string))