from unicodedata import name

#li = { chr(i) for i in range(1,256)}
#print(li)
li = { chr(i) for i in range(1,256) if 'SIGN' in name(chr(i),'')}
print(li)