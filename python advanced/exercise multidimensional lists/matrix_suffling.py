def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def is_valid_coord(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

def swap_elements(matrix, row1, col1, row2, col2):
    if is_valid_coord(matrix, row1, col1) and is_valid_coord(matrix, row2, col2):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        return True
    return False

rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    if command.startswith("swap"):
        tokens = command.split()
        if len(tokens) == 5:
            row1, col1, row2, col2 = map(int, tokens[1:])
            if swap_elements(matrix, row1, col1, row2, col2):
                print_matrix(matrix)
                continue
    print("Invalid input!")


