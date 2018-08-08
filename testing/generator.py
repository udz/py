# generator.py

# top level syntax, function --> underscore method
# x()   __call__

def add1(x,y):
    return x + y

class Adder:
    def __call__(self,x,y):
        return x+ y

add2 = Adder()

print(add1(1,4))
print(add2(1,4))

'''
for _ in range(10):  # where _ is the throwable variable
    pass
'''