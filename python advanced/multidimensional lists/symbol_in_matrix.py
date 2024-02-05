n = int(input())

# Input: Matrix values
matrix = []
for _ in range(n):
    row = input()
    matrix.append(row)

# Input: Symbol to search for
symbol = input()

# Find the position of the first occurrence of the symbol
found = False
for row_index, row in enumerate(matrix):
    for col_index, char in enumerate(row):
        if char == symbol:
            print(f"({row_index}, {col_index})")
            found = True
            break
    if found:
        break

# If the symbol is not found, print a message
if not found:
    print(f"{symbol} does not occur in the matrix")