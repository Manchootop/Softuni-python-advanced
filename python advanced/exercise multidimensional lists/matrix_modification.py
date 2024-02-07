def is_valid_coordinate(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

def add_value(matrix, row, col, value):
    if is_valid_coordinate(matrix, row, col):
        matrix[row][col] += value
    else:
        print("Invalid coordinates")

def subtract_value(matrix, row, col, value):
    if is_valid_coordinate(matrix, row, col):
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Read matrix dimensions
n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Process commands
while True:
    command = input()
    if command == "END":
        break
    command_parts = command.split()
    action = command_parts[0]
    row, col, value = map(int, command_parts[1:])
    if action == "Add":
        add_value(matrix, row, col, value)
    elif action == "Subtract":
        subtract_value(matrix, row, col, value)

# Print the resulting matrix
print_matrix(matrix)
