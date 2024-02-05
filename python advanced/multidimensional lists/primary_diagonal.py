# Input: Size of the square matrix
n = int(input())

# Input: Matrix values
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Calculate and print the sum of the primary diagonal
diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]

print("Sum of the primary diagonal: ", diagonal_sum)


