import os

path = os.getcwd()

sourceFile = open(os.path.join(path,'zeroDivide.py'),'r')

content = sourceFile.read()
sourceFile.close()
print(content)


sourceFile = open(os.path.join(path,'abc.txt'),'a')
sourceFile.write(content)
sourceFile.close()

