import pprint
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
pprint.pprint(theBoard)

theBoard['mid-M'] = 'X'
theBoard['low-M'] = 'O'
theBoard['top-L'] = 'X'
theBoard['low-R'] = 'O'
theBoard['top-R'] = 'X'
theBoard['top-M'] = 'O'
theBoard['low-L'] = 'X'

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)