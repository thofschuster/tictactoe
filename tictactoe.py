from __future__ import print_function
from IPython.display import clear_output


def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

board = ['X'] * 10
display_board(board)


def player_input():
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = raw_input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

player_input()

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the mark left
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) #diagonal


import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '
