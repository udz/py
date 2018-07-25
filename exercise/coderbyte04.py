# Determine the largest word in the string

string = 'My Name is Ujjwal'

def longest_word(str):
    longest_word = ''
    length = 0
    for word in str.split():
        if len(word) > length:
            longest_word = word
            length = len(word) 
    return longest_word    

print(longest_word(string))