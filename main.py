import random
import numpy as np


def print_board(board):
    for row in board:
        print(row)
    print()


# a kiralynok permutacioja
def random_permutation(n):
    initial_placement = list(range(n))
    random.shuffle(initial_placement)

    board = np.zeros((n, n), dtype=int)
    for i in range(n):
        board[i][initial_placement[i]] = 1

    return board, initial_placement


# kicserel ket sort a tablan
def swap(board, i, j):
    board[i], board[j] = board[j].copy(), board[i].copy()


# megnezi, hogy a csere utan mekkora lenne az utkozesek szama
def check_swap(board, queens, mdiag, sdiag, i, j):
    swap(board, i, j)
    mdiag[n - i + queens[i] - 1] -= 1
    sdiag[i + queens[i]] -= 1
    mdiag[n - j + queens[j] - 1] -= 1
    sdiag[j + queens[j]] -= 1
    queens[i], queens[j] = queens[j], queens[i]
    mdiag[n - i + queens[i] - 1] += 1
    sdiag[i + queens[i]] += 1
    mdiag[n - j + queens[j] - 1] += 1
    sdiag[j + queens[j]] += 1

    col_sum = 0
    for i in range(len(board) * 2 - 1):
        if mdiag[i] > 1:
            col_sum += 1
        if sdiag[i] > 1:
            col_sum += 1

    return col_sum


# leellenorzi, hogy egy kiralynot utnek-e
def is_attacked(mdiag, sdiag, i, j, n):
    if mdiag[n-i+j-1] > 1: return True
    if sdiag[i+j] > 1: return True
    return False


# megszamolja, hogy hany kiralyno van az atlokon
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


# a fo fuggveny
def n_sosic(n):
    solved = False
    while not solved:
        board, queens = random_permutation(n)
        mdiag, sdiag, n_collision = check_diag(board)
        n_swaps = -1
        while n_swaps != 0:
            n_swaps = 0
            for i in range(n-1):
                for j in range(1, n):
                    if is_attacked(mdiag, sdiag, i,  queens[i], n) or is_attacked(mdiag, sdiag, i, queens[j], n):
                        new_col = check_swap(board.copy(),queens.copy(), mdiag.copy(), sdiag.copy(), i, j)
                        if new_col < n_collision:
                            swap(board, i, j)
                            mdiag[n-i+queens[i]-1] -= 1
                            sdiag[i+queens[i]] -= 1
                            mdiag[n - j + queens[j] - 1] -= 1
                            sdiag[j + queens[j]] -= 1
                            queens[i], queens[j] = queens[j], queens[i]
                            mdiag[n - i + queens[i] - 1] += 1
                            sdiag[i + queens[i]] += 1
                            mdiag[n - j + queens[j] - 1] += 1
                            sdiag[j + queens[j]] += 1
                            n_collision = new_col
                            n_swaps += 1
        if n_collision == 0:
            solved = True
    return board, queens


n = int(input("Number of queens: "))

board, queens = n_sosic(n)

if n < 30:
    print_board(board)

print("queens: {}".format(queens))