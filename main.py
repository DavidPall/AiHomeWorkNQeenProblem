import random
import numpy as np

def print_board(board):
    for row in board:
        print(row)

print("Szia Robiii. :D")

n = int(input("Number of queens: "))

initial_placement = list(range(n))
random.shuffle(initial_placement)

board = np.zeros((n,n), dtype=int)
for i in range(n):
    board[i][initial_placement[i]] = 1

print_board(board)