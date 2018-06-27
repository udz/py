# Dictionary uses key:value pair. key could be of any data type
# Dictionaries are not ordered

apple = {'name':'green apple'
         ,'color':'Green'
         ,'taste':'bitter'
         }

for key,value in apple.items():
    print('%s --> %s' %(key,value))

for v in apple.values():  # same could be done with keys()
    print('%s' %(v))
    
print(apple['name'])

print(list(apple.items()))

print(list(apple.keys()))

print('bitter' in apple.values()) # same could be done with keys()
print('name' in apple) # same as 'name' in apple.keys()

print('I am eating '+str(apple.get('name','Red apple')) + '.') # If 'name' doesn't exist default value will be displayed

# Dictionary of list
dictionary = {'names':['Ram','Shyam','Hari'], 'age':[2]}
dictionary['age'].append(3)
print(dictionary)
