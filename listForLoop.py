# This program lets user view the available items in the supplies list
# Further user can add new items to the list

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print(str('pens' in supplies))
print(str('cats' not in supplies))

while True:
    item = input('Enter item to include in the list: ')
    if item in supplies:
        print(str(item)+ ' already exist in the supplies!')
        continue
    elif item=='':
        break   # if empty item is entered
    else:
        supplies += [item]
        print('Item Added Successfully')

print('\n\nThe available items in the supplies are')
for item in range(len(supplies)):
    print('Item['+str(item)+'] : '+str(supplies[item]))

