# Count the vowels in the string
# Count the words in the string

string = 'My o my eio asdf sdf sd'

def count_vowel(str):
    count = 0
    for char in str:
        if char in 'aeiou':
            count += 1
    return count

def count_word(str):
    count = len(str.split())
    return count

print(count_word(string))
#print(count_vowel(string))
