#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(board)])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row] = -1

def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    solve_n_queens_util(board, 0, n, solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_n_queens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
