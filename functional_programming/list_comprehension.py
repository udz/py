# List comprehension

# Syntax
# [function for item in iterable]

li = [-1,-3,1,3,5,7,9]
print([x**x for x in li])

# List square of all numbers greater than 1
new_li = list(map(lambda x: x*x, list(filter(lambda x: x>1,li))))
print(new_li)
new_li = [x*x for x in li if x>1]
print(new_li)

# Square all the numbers less than 0
less_than_0 = [x*x for x in li if x<0]
print(less_than_0)

