def read_matrix():
    size = int(input())
    matrix = [list(map(int, input().split(', '))) for _ in range(size)]
    return matrix

def find_diagonals(matrix):
    size = len(matrix)
    primary_diagonal = [matrix[i][i] for i in range(size)]
    secondary_diagonal = [matrix[i][size - i - 1] for i in range(size)]
    return primary_diagonal, secondary_diagonal

matrix = read_matrix()
primary_diagonal, secondary_diagonal = find_diagonals(matrix)

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")


