import random
import numpy as np

def print_board(board):
    for row in board:
        print(row)

def random_permutation(n):
    initial_placement = list(range(n))
    random.shuffle(initial_placement)

    board = np.zeros((n, n), dtype=int)
    for i in range(n):
        board[i][initial_placement[i]] = 1

    return board, initial_placement

def swap(board, i, j):
    board[i], board[j] = board[j], board[i]

def check_swap(board, i, j):
    swap(board, i, j)
    mdiag, sdiag, mcollision, scollision = check_diag(board)
    return mcollision + scollision

def is_attacked(mdiag, sdiag, i, j, n):
    if mdiag[n-i+j-1] > 1: return True
    if sdiag[i+j] > 1: return True
    return False


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
                        new_col = check_swap(board.copy(), i, j)
                        if new_col < n_collision:
                            swap(board, i, j)
                            mdiag[n-i+queens[i]-1] -= 1
                            sdiag[i+queens[i]] -= 1
                            mdiag[n - j + queens[j] - 1] -= 1
                            sdiag[j + queens[j]] -= 1
                            swap(queens, i, j)
                            mdiag[n - i + queens[i] - 1] += 1
                            sdiag[i + queens[i]] += 1
                            mdiag[n - j + queens[j] - 1] += 1
                            sdiag[j + queens[j]] += 1
                            n_collision = new_col
                            n_swaps += 1





n = int(input("Number of queens: "))

board, init = random_permutation(n)