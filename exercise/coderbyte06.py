# Factorial

number = int(input('Please enter the number of which to find factorial: '))

def find_factorial(num):
    factorial = 1
    for i in range(1,num+1):
        factorial *= i
    return factorial

print(find_factorial(number))