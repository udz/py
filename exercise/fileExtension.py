'''
Write a python program that takes a list of file extensions and prints all the files from the current
directory matching the extension given.
'''
import os

extensions = ['exe','py','xlsx']

print(os.getcwd())

for file1 in os.listdir('.\\'):
    parts = file1.split('.')
    #print(parts)
    if parts[len(parts)-1] in extensions:
        print(file1)
