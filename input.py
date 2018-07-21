

name = input('Please enter your name: ')
age = input('Please enter your age: ')

try:
    age = int(age)
    print(age)
except Exception as err:
    print('Age is invalid ',err)