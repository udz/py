a,b = 5,6 # Multi Assignment
a,b = b,a # Swap values

string = ['My','name','is','Ujjwal']
print(' '.join(string))

# Most frequent item in the list
lists = [1,2,2,3,3,4,4,4,5,1,2,4]
print(max(set(lists),key=lists.count))

# Usign counter from Collection
from collections import Counter
cnt = Counter(lists)
print(cnt.most_common(3)) 

# Check if the words are anagram
str1,str2 = 'Ujjwal','jjUawl'
print(Counter(str1)==Counter(str2))

# reverse a string / list
print(str1[::-1])

# print char from a string/list in reverse order
for char in reversed(str1):
    print(char)

integer = 1234567
# reversing integer
print(int(str(integer)[::-1])) 

# transpose 2d array
original =[['a','b'],['c','d'],['e','f']]
transposed = zip(*original)
print(list(transposed))

# chained comparison
print(a,b)
print(a>b==5)

# Chained function call
# Calling difference function based on same argument depending on condition
c = False
def product(a,b):
    return a*b
def add(a,b):
    return a+b

result = (product if c else add)(5,6)
print(result)

# copy list
list1 = [1,2,3,4]
list2 = []

list2 = list1
print(list2)

# deep copy
from copy import deepcopy
l1 = [[1,2],[3,4]]
l2 = deepcopy(l1)
# l2 = l1 # This works as well
print(l2)

# Returning None or default value when the key is not in the dectionary
d = {'a':1,'b':2}
print(d.get('c',3))

# For else
# else gets called when for loop doesn't reach break statement
for ele in list1:
    if ele==0:
        break
else:
    print("Didn't break out of loop")

# Join list elements
# converts list to comma separated string
list3 = ['a','b','c']
print(','.join(list3))

# convert list of integer to comma separated
list1 = [1,2,3,4]
print(','.join(map(str,list1)))

# merge dicts
d1 = {'a':1}
d2 = {'b':2}
print({**d1,**d2})  # Method 1

print(dict(d1.items()|d2.items()))  # Method 2

d1.update(d2)  # Method 3
print(d1)

# Find index of min / max

lst = [33,45,67,11]
def minIndex(lst):
    return min(range(len(lst)),key =lst.__getitem__)
def maxIndex(lst):
    return max(range(len(lst)),key =lst.__getitem__)

print('Index of minimum value in list is',minIndex(lst))
print('Index of maximum value in list is',maxIndex(lst))

# remove duplicate items from the list
list1 = [1,3,4,3,4,5,6,6]
print(list(set(list1)))   # doesn't keep order

from collections import OrderedDict  # maintain order
list2 = ['ss','dd','dd','ss','zz']
print(list(OrderedDict.fromkeys(list2).keys()))

# Count of each item
dd = dict((i,list2.count(i)) for i in list2)
print(dd)
