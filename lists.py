# Lists, indices, slice

empty = []
a = [1,2,3,4]
b = ['a','b',12, None, True]
c = [a,b]

print(a,b) # [1,2,3,4] ['a','b',12, None, True]

print(a[0],a[3]) # 1 4
print (c[0][2]) # [3]

# Negative indices
print(a[-1]) # [4]

# Sublists using slices
print(a[0:2]) # slice [1,2]
print(a[:3]) # [1,2,3]
print(a[1:]) # [2,3,4]

# Getting length of list
print(len(a)) # 4

# Changing list values
a[0] = 24
print(a[0]) # 24

# List concatination and list replication
print(a+b)
print (a*2)

# Removing values in list
del a[0]
print(a)

