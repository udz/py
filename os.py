import os

for folderName, subFolders, filenames in os.walk('d:\\Learning\\BLOG'):
    print('CURRENT FOLDER '+ folderName)

    for subFolder in subFolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subFolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName +': '+ filename)

    print(' ')

    #print(folderName,subFolders,filenames)
