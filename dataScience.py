"""
import os

os.getcwd()

path = './Data Sets/Kaggle'
dataFile = '65worldindexes.csv'

os.chdir(path)
dataFile = open(dataFile,'r')
data = []
data = dataFile.readline().split(',')
print(data)
"""

import os
#os.getcwd()

path = './Data Sets'
dataFile = 'Alice.txt'

os.chdir(path)

"""
dataFile = open(dataFile,'r')
line = dataFile.readline().split(' ')
print(line)
"""
words = 0
story = ''
with open(dataFile,'r') as f:
    for line in f:
        story += line
        words += len(line.split(' '))

print('='*60)

print('The story has total ' + str(words) + ' words')

dataFile2 = open('Bob.txt','w')
dataFile2.write(story)
dataFile2.close()

"""
line.sort()  #none
print('='*60)
print(line.pop())
print('='*60)
line.remove('Alice') # none
print('='*60)
print(line)
print('='*60)
line.reverse()
print(line)
"""