rows = int(input())
#
# flattening_matrix = [
#     [int(num) for num in input().split(', ')]
#     for _ in range(rows)
# ]
#
# print(flattening_matrix)

matrix = [input().split(', ') for row in range(rows)]



flattening_matrix = [int(num) for row in matrix for num in row]

print(flattening_matrix)