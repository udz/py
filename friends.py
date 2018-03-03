# Enter friend names which will print out 
friends = []
while True:
    name = input('Enter your friend\'s name: ')
    if name == '':
        break
    friends += [name]
print('Your friends list is ')
for name in friends:
    print (' ' + name)
