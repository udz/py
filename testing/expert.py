#from inspect import getsource
# decorator

from time import time

def timer(func):
    def wrapper(*args,**kwargs):
        before = time()
        rv = func(*args,**kwargs)
        after = time()
        print('elapsed',after - before)
        return rv
    return wrapper

@timer
def add(x,y=10):
    return x + y
#add = timer(add)

@timer
def sub(x,y=10):
    return x - y
#sub = timer(sub)

print('add(10)', add(10))
print('add(20,30)', add(20,30))
print('add("a","b")',add("a","b"))
print('sub(10)', sub(10))
print('sub(20,30)', sub(20,30))
