# collatz sequence
# will only exit if the return value is 1 otherwise detect if the entered number is even or off

def collatz(number):
    if (number%2==0):
        print('Even: '+ str(number//2))
        return int(number//2)
    else:
        print('Odd: '+ str(3*number +1))
        return int(3*number +1)

while True:
    print('Enter number ')
    x = input()
    try:
        value=collatz(int(x))
        if value==1:
            break
    except:
        print('Please enter an integer')
        
print('---End---')
