
# Syntax
# lambda parm: function
square = lambda x: x*x
print(square(2))

# Syntax
# map(function, iterable)
li = [-1,-2,1,3,4,5]
new_li = list(map(lambda x: x*x,li ))
print(new_li)

# Syntax
# reduce(function, list)
from functools import reduce 
print(reduce(lambda x,y:x*y,li))

# Syntax
# filter(function, list)
print(list(filter(lambda num:num<0, li)))
