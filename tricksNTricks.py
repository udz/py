import copy

# Multiple assignment trick

dog = ['black',
       'German Shephard',
       'huge']

color,breed,size = dog

print(color,breed,size)

a,b, = 'Ujjwal','Ram'
print(a,b)
a,b = b,a  # swap values
print(a,b)

# Augmented assignment

# index(), append() - end of the list, del, insert() - any point

supplies = ['eggs','knife','pan','bucket']
print(supplies)
print(str(supplies.index('eggs')))
supplies.append('cooker')
supplies.insert(1,'skewers')
print(supplies)

supplies.reverse()  # reverses the order ragardless of the ascending or descending 
print('Reverse order: '+str(supplies))

supplies.sort(reverse=True)
print('Descending: '+str(supplies))

# del removes if we know the index, remove() removes if we know the value
del supplies[0]
print(supplies)
supplies.remove('eggs')
print(supplies)

# sort() uses ASCIIbetical order hence use str.lower

supplies.sort(key=str.lower)

# continuation of code in next line by the use of \
print('This is a test' + \
      ' message ' + \
      str(supplies))


# Tuple is different than list because they use () instead of [] and are immutable
# tuples have better performance than lists and are used when the value doesn't need
# to be changed again and again
tuplies = tuple(supplies)
print(tuplies)

print(list('Hi'))

# References - lists are referenced rather than copied


# string is like a list, but is immutable. i.e. values couldn't be appended or deleted later

# copy list using copy.copy() or copy.deepcopy() if the list contains lists 

# import copy
optional = copy.copy(supplies)
optional[1] = 'Changed'
print(optional)
print(supplies)
