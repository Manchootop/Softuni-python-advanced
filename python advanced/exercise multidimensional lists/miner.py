def detonate_bomb(matrix, row, col):
    bomb_value = matrix[row][col]
    matrix[row][col] = 0
    n = len(matrix)
    for i in range(max(0, row-1), min(n, row+2)):
        for j in range(max(0, col-1), min(n, col+2)):
            if not (i == row and j == col):
                matrix[i][j] -= bomb_value
                if matrix[i][j] < 0:
                    matrix[i][j] = 0

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Parse input
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
bombs = list(map(lambda x: tuple(map(int, x.split(','))), input().split()))

# Detonate bombs
for bomb in bombs:
    detonate_bomb(matrix, bomb[0], bomb[1])

# Count alive cells and calculate sum
alive_count = 0
alive_sum = 0
for row in matrix:
    alive_count += len([cell for cell in row if cell > 0])
    alive_sum += sum(cell for cell in row if cell > 0)

# Output
print(f"Alive cells: {alive_count}")
print(f"Sum: {alive_sum}")
print_matrix(matrix)
