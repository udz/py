''' 
A Shelf file stores the content in the binary mode
It is advisable to use the shelf file to store program generated data unless it needs to be readable in text editor
There will be three files created with each instance of the shelf file .bak, .dat and .dir files

The file when opened permits reading and writing at once
'''

import shelve
import os
path = os.getcwd()
print(path)

shelfFile = shelve.open('.\\myData')

# Uncomment Following codes to save values to the shelf file 
#names = ['Ram','Shyam','Hari']
#Address = ['Jhochhen','Patan','Panipokhari']
#shelfFile['names']=names
#shelfFile['Address']=Address

print(shelfFile['names'])
print(shelfFile['Address'])

print(list(shelfFile.keys()))
print(list(shelfFile.values()))


shelfFile.close()

