passwordFile = open('Read.txt')
secretPassword = passwordFile.read()
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')

#Valid variables

SPAM = 'spam'
spam = 'egg'

print(SPAM+' '+spam)

print(secretPassword)

print(len('Ujjwal'))

print('I am '+str(43)+' years old')

# float() int() str()
# rount()

# // % / **

isTrue = True
print(isTrue)

a=2
b=3

print(not(a==b)and not(b==a))

name = 'Dracula'
age = 15
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print("I don't know who you are")


while True:                         # (1)
    print('Please type your name.')
    name = input()                  # (2)
    if name == 'your name':         # (3)
        break                       # (4)
print('Thank you!')   
    

while True:
  print('Who are you?')
  name = input()
  if name != 'Joe':       #(1)
    continue              #(2)
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = input()      #(3)
  if password == 'swordfish':
    break                 #(4)
print('Access granted.')  #(5)


