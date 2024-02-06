def generate_palindrome_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            # Calculate the middle letter based on the row and column index
            middle_letter = chr(ord('a') + i + j)
            # Construct the palindrome by concatenating the first letter, middle letter, and last letter
            palindrome = chr(ord('a') + i) + middle_letter + chr(ord('a') + j)
            row.append(palindrome)
        matrix.append(row)
    return matrix

rows, columns = map(int, input().split())
palindrome_matrix = generate_palindrome_matrix(rows, columns)

for row in palindrome_matrix:
    print(' '.join(row))

