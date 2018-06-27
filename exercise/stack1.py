'''
k = 'rep'
x = 10
#b = a*i
#
rep = [k * i for i in range(1,x,1)]
print(rep)
'''

import json

string = 'abc,bcd,dgdf'
print(string.split(','))


# following code assumes that 'data.json' file exists in the current working directory
with open('data.json', 'r') as jsonFile: # opens JSON file in read only mode
    # loads the content of JSON file and converts it into python dictionary object
    dictionary = json.load(jsonFile)
    print(dictionary)