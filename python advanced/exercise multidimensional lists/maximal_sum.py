def find_max_sum_submatrix(matrix):
    max_sum = float('-inf')
    max_submatrix = []

    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            submatrix_sum = sum(matrix[i][j:j+3]) + sum(matrix[i+1][j:j+3]) + sum(matrix[i+2][j:j+3])
            if submatrix_sum > max_sum:
                max_sum = submatrix_sum
                max_submatrix = [matrix[i][j:j+3], matrix[i+1][j:j+3], matrix[i+2][j:j+3]]

    return max_sum, max_submatrix

rows, columns = map(int, input().split())
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

max_sum, max_submatrix = find_max_sum_submatrix(matrix)

print(f"Sum = {max_sum}")
for row in max_submatrix:
    print(' '.join(map(str, row)))

