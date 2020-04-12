import random
import numpy as np


def print_board(board):
    for row in board:
        print(row)


def check_diag(board):
    mdiag = np.zeros(len(board)*2 - 1, dtype=int)
    sdiag = np.zeros(len(board)*2 - 1, dtype=int)

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                sdiag[i+j] += 1
                mdiag[len(board) - i + j - 1] += 1

    col_sum = 0
    for i in range(len(board) * 2 - 1):
        if mdiag[i] > 1:
            col_sum += 1
        if sdiag[i] > 1:
            col_sum += 1

    return mdiag, sdiag, col_sum


n = int(input("Number of queens: "))

initial_placement = list(range(n))
random.shuffle(initial_placement)

board = np.zeros((n,n), dtype=int)
for i in range(n):
    board[i][initial_placement[i]] = 1

check_diag(board)