# Change the string to Proper Case

string = 'my name is ujjwal'

def ProperCase(str):
    new_word = ''
    for word in str.split():
        count = 1
        for letter in word:
            if count == 1:
                letter = letter.upper()
            count += 1
            new_word += letter
        new_word += ' '
    return new_word

print(ProperCase(string))