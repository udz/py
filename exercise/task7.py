'''
Write a program that takes a file name from command line and prints the number of lines in that file. If the provided argument
does not refer to a file an error should be printed. Example Usage:

python countlines.py /etc/shells
11

python countlines.py /foo/bar
Sorry, file /foo/bar not found
'''
import sys

# Efficient way of counting lines of file
# https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def file_len(*args):
    try:
        with open(sys.argv[1]) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
    except:
        message = 'Sorry, file ' + sys.argv[1] + ' not found'
        return message
'''
# shortest implementation
num_lines = sum(1 for line in open('myfile.txt'))
'''

'''
# not so efficient as the variable line gets initialized which loads file content during runtime
def file_len(*args):
    i = 0
    try:
        file = open(sys.argv[1],'r')
        for line in file:
            i += 1
        return i    
    except:
        message = 'Sorry, file ' + sys.argv[1] + ' not found'
        return message
'''

print(file_len())
