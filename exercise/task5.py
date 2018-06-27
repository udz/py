'''
Write a function that takes a list of strings AND a minimum length (number) and returns only the strings that are longer than
the provided number. Example Usage:

# returns the list: ['baby', 'more', 'time']
longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')
'''

list_of_words = ['What','is','the','name','of','the','movie','?']

def longer_than(number,word_list):
    result = []
    i = 0
    for word in word_list:
        if len(word) >= int(number):
            result.insert(i,word)
            i += 1
    return result

print(longer_than(4,list_of_words))