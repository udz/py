# Function as parameter
def sum(a,b):
    return a + b

def returnA():
    return 10

def returnB():
    return 20

print(sum(returnA(),3))

# Function as return value
def some_function(a):
    if a =='a':
        return returnA()
    elif a == 'b':
        return returnB()

print(some_function('b'))