'''
Four ways of handling String in Python
'''

name = 'Ujjwal'
a = 5
b = 10
number = 9808249910
question = 'up'
errno = 50159747054

# String Interpolation Method. Python 3.6 and above
print(f"{name} is my name")
print(f"{a} + {b} is {a+b}")

# Python 3 and above
print('Hey {}'.format(name))
print('Hey {name1}! My number is {phone}'.format(name1 = name,phone = number))

# Old method comparable to printf of C and C++
print("Hey %s, what's %s?" %(name,question))
print('Hey %(name)s, there is a 0x%(errno)x error!' % {"name": name, "errno": errno })
print('Hello %(name1)s' %{"name1":name})

'''
# Template method
from string import Template
t = Template('Hey, $name!')
print(t.substitute(name=name))
'''