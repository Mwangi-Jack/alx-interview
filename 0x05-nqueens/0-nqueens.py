#!/usr/bin/python3
"""Backtracking Algorithm"""

import sys


def is_safe(board, row, col, N):
    """This methos finds if it is safe to place a queen on a board"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col, N, solutions):
    """This method finds all the possible solutions"""
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, N, solutions) or res
            board[i][col] = 0

    return res


def print_solutions(solutions):
    """This method prints all the possible solutions"""
    for sol in solutions:
        print(sol)


def main():
    """Main function """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
