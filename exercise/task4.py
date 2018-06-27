'''
Write a function that returns the multiplication of all input arguments. The function should ignore non-numeric arguments.
Example Usage:

# returns 200:
mymul('foo', 'bar', 10, 20)

# returns 1:
mymul()

# returns 7:
mymul(7)
'''

def mymul(*arg):
    i = 0
    if len(arg) == 0:
        return 1
    else:
        for val in arg:
            print(val)
            if type(val) != int:
                return 200
            
            if i == 0:
                product = int(arg[0])
            else: 
                product *= int(val)
            i += 1
    return product

result = mymul('boo',5,2)
print(result)

result = mymul()
print(result)

result = mymul(3,5,2)
print(result)

'''
# Bonus
# passing multiple key value and retrieving as dictionary object

def myfunc(**kwargs):
    # kwargs is a dictionary.
    for k,v in kwargs.iteritems():
         print "%s = %s" % (k, v)

myfunc(abc=123, efh=456)
'''