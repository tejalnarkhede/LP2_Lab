import random

def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    stack = [(board, 0)]
    while stack:
        board, row = stack.pop()
        if row == n:
            solutions.append(board[:])
        else:
            for col in range(n):
                if is_valid(board, row, col):
                    new_board = board[:]
                    new_board[row] = col
                    stack.append((new_board, row + 1))

    random.shuffle(solutions)
    print("Total solutions:", len(solutions))
    solution_count = int(input("Enter solution count: "))
    print()
    for solution in solutions[:solution_count]:
        print_solution(solution)
        print()

def print_solution(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += "- "
        print(line)

# Example usage
n = int(input("Enter the size of the chessboard: "))
solve_n_queens(n)