import pprint

items = {'name':''
         ,'gender':''}

items['name']= input('Enter your name: ')
items['age']= input('Enter your age: ')

print(items.get('name','Default') + ' ' + items.get('age','11'))

pprint.pprint(items)
