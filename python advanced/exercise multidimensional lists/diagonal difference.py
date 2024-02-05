def read_matrix():
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    return matrix

def find_diagonal_sums(matrix):
    size = len(matrix)
    primary_sum = sum(matrix[i][i] for i in range(size))
    secondary_sum = sum(matrix[i][size - i - 1] for i in range(size))
    return primary_sum, secondary_sum

matrix = read_matrix()
primary_sum, secondary_sum = find_diagonal_sums(matrix)

absolute_difference = abs(primary_sum - secondary_sum)
print(absolute_difference)
