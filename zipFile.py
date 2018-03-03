import zipfile, os

example = zipfile.ZipFile('practice.zip')

print(example.namelist())
information = example.getinfo('practice/sum1-100.py')

print(information.file_size)
print(information.compress_size)

print('Compress size is %sx smaller than original' %(round(information.file_size/information.compress_size,2)))

example.close()