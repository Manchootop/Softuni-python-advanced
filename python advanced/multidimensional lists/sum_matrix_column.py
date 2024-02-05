# rows, columns = input().split(', ')
# matrix = [input().split() for row in range(int(rows))]
#
# for column in range(int(columns)):
#     for row in range(int(rows)):
#         print(matrix[column][row])

# print(matrix)
#
# for row in range(rows):
#     row_input = input().split()
#     for column in range(columns):
#         pass



# matrix_sizes = input().split(', ')
# rows, columns = int(matrix_sizes[0]), int(matrix_sizes[1])
#
# # Input: Elements of the matrix
# matrix = [map(int, input().split()) for _ in range(rows)]
#
# # Calculate the sum for each column
# column_sums = [sum(column) for column in zip(*matrix)]
#
# # Printing the sum for each column
# for col_sum in column_sums:
#     print(col_sum)



# matrix_sizes = input().split(', ')
# rows, columns = int(matrix_sizes[0]), int(matrix_sizes[1])

# Input: Elements of the matrix
# matrix = [input().split() for _ in range(rows)]
#
# column_sums = [0] * columns
#
# for r in range(rows):
#     for c in range(columns):
#         value = int(matrix[r][c])
#         column_sums[c] += value
#
# for column in range(columns):
#     print(column_sums[column])
#

# rows, columns = input().split(', ')
# matrix = [input().split() for row in range(int(rows))]
#
# for column in range(int(columns)):
#     for row in range(int(rows)):
#         print(matrix[column][row])
#


# Input: Matrix sizes in format "{rows}, {columns}"
matrix_sizes = input().split(', ')
rows, columns = int(matrix_sizes[0]), int(matrix_sizes[1])

# Input: Elements of the matrix
matrix = [list(map(int, input().split())) for _ in range(rows)]

# Calculate the sum for each column
for column in zip(*matrix):
    print(column)
column_sums = [sum(column) for column in zip(*matrix)]

# Printing the sum for each column
for col_sum in column_sums:
    print(col_sum)