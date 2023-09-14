def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            print(board[i])
            return False
    return True


def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def backtrack(row):
     
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


# Get the value of 'n' from the user
n = int(input("Enter the value of 'n': "))

# Solve the N-Queens problem using Backtracking
solutions = solve_n_queens(n)

# Print at least two solutions
if len(solutions) < 2:
    print("Only one solution found.")
else:
    print("Solution 1:")
    for row in solutions[0]:
        line = ['-'] * n
        line[row] = 'Q'
        print(' '.join(line))
    print("\nSolution 2:")
    for row in solutions[1]:
        line = ['-'] * n
        line[row] = 'Q'
        print(' '.join(line))
