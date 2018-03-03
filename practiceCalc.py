while True:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    o = input('Enter Operation: '
              '\n   "a" to add'
              '\n   "s" to subtract'
              '\n   "m" to multiply'
              '\n   "d" to divide'
              '\nOR "q" to quit: ')

    if o=='a':
        result = a+b
        operation = 'addition'
    elif o=='s':
        result = a-b
        operation = 'subtraction'
    elif o=='m':
        result = a*b
        operation = 'multiplication'
    elif o=='d':
        result = a/b
        operation = 'division'
    elif o=='q':
        break
    else:
        print('Invalid Operation. Please Try Again')
        continue
    print('\nThe Result for '+ operation + ' operation is: '+ str(result) +'\n')

print('End')
