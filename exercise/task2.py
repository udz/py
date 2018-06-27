'''
Write a program that takes a file name as command line argument,
count how many times each word appears in the file and prints the word that appears the most
(and its relevant count)
'''
import sys
import pprint

file = sys.argv[1]
#file = open('exercise/task1.py','r')
#file = 'exercise/words.txt'
words = []

'''
# Method 1
def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

words = read_words(file)
'''
# Method 2
with open(file,'r') as f:
    words = f.read().split()

# Create a dictionary of the words and their occurrances
count = {}
for word in words:
    if word in count:
        count[word] = count.get(word,0) + 1
    else:
        count[word] = 1

print('\nTotal words appearing in the file and their number of occurarnces are as follows')
pprint.pprint(count)

maximum_occurrance = max(count, key=count.get)  # limitation of this method is this only captures the first occurrance

# Print the key, value of the word that occurred maximum number of times
# print(str(maximum_occurrance) + ' - ' + str(count.get(maximum_occurrance,0)))

maxx = max(count.values())

results = {}
for word in count:
    if count.get(word,0)==maxx:
        results[word] = maxx

print('\nThe word(s) having highest occurrances are:')
pprint.pprint(results) 