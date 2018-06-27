'''
Write a function that takes a number and returns the sum of its digits. 
Raise exception if argument of the wrong type was passed
'''

# The function that takes the number and returns sum
def sum_of_digits(value):
    string = str(value)
    sum = 0
    for digit in string:
        sum += int(digit)
    return(sum)

number = input('Enter number of which to find sum of digits: ')
#if type(number) != int:
#    raise ValueError('Entered value is not an integer')

total = sum_of_digits(number)
print('The Sum of the digits is: ' + str(total))
    

