import os

myFiles = ['Read.txt','test.txt']

# path = os.path.join('D:','\\Learning','Programming','Python')

path = os.getcwd()

for filename in myFiles:
    path1 = os.path.join(path,filename)
    print(path1)
    print(os.path.split(path1))
    #print(os.path.join('.\\',filename))
    print('Directory Name is: ' + os.path.dirname(path1))
    print('Basename is: ' + os.path.basename(path1))
    print('Relative Path is: '+ os.path.relpath(path1,'E:\\'))
    print('Absolute Path is: '+os.path.abspath('.'))
    print(os.path.isabs('.')) # FALSE since . is relative path
    print(path1.split(os.path.sep))  # Split on the path separator
    print(os.path.isfile(path1))


# File list display
totalSize = 0
for file in os.listdir('.\\'):
    size = os.path.getsize(file)
    print(file.ljust(40,'.') + str(size).rjust(10) + ' Bytes')
    totalSize += size
print('\nTotal File Size is: '.ljust(40,'.') + str(totalSize).rjust(10)+ ' Bytes')

print(os.path.exists('.\\Projects'))
print(os.path.exists('E:\\'))
#os.makedirs('.\\ABC')
print(os.path.exists('.\\ABC'))
