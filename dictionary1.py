import pprint
from collections import defaultdict

items = {'name':''
         ,'age':''}
items = defaultdict(lambda: 'unknown')

items['name']= input('Enter your name: ')
items['age']= input('Enter your age: ')

print(items.get('name','Default') + ' ' + items.get('age','11') + ' ' + items['gender'])

#pprint.pprint(items)
