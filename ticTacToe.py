
# Tic Tac Toe board representation

ticTacToe = {'top-L':' ','top-M':' ','top-R':' ',
             'mid-L':' ','mid-M':' ','mid-R':' ',
             'low-L':' ','low-M':' ','low-R':' '}
turn = 'X'

def printBoard():
    print(ticTacToe['top-L'] + ' | ' + ticTacToe['top-M'] + ' | ' + ticTacToe['top-R'])
    print ('----------')
    print(ticTacToe['mid-L'] + ' | ' + ticTacToe['mid-M'] + ' | ' + ticTacToe['mid-R'])
    print ('----------')
    print(ticTacToe['low-L'] + ' | ' + ticTacToe['low-M'] + ' | ' + ticTacToe['low-R'])

for i in range(9):
    position=input('Enter position for ' + turn + ': ')
    ticTacToe[position] = turn
    printBoard()
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'


