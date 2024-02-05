rows = int(input())
#
# even_matrix = [x for x in range(rows) for num in input().split(', ')]
# even_matrix1 = [int(num) for num in row.split(', ') if int(num) % 2 == 0 for row in input]
# print(even_matrix)


even_matrix = [
    [int(num) for num in input().split(', ') if int(num) % 2 == 0]
    for _ in range(rows)
]

print(even_matrix)