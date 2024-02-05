# Input: Matrix sizes
rows, columns = map(int, input().split(", "))

# Input: Matrix values
matrix = []
for _ in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

# Initialize variables to store the maximum submatrix and its sum
max_submatrix_sum = float('-inf')
max_submatrix = []

# Iterate through the matrix to find the maximum 2x2 submatrix
for i in range(rows - 1):
    for j in range(columns - 1):
        submatrix_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if submatrix_sum > max_submatrix_sum:
            max_submatrix_sum = submatrix_sum
            max_submatrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]

# Print the found submatrix and its sum
print(f"Sum = {max_submatrix_sum}")
for row in max_submatrix:
    print(" ".join(map(str, row)))
