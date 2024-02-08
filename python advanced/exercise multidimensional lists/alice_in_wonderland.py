def move_alice(matrix, row, col, command):
    directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    max_rows = len(matrix)
    max_cols = len(matrix[0])

    if command in directions:
        d_row, d_col = directions[command]
        new_row, new_col = row + d_row, col + d_col

        if 0 <= new_row < max_rows and 0 <= new_col < max_cols:
            return new_row, new_col
        else:
            return None, None
    else:
        return None, None


def main():
    n = int(input())
    field = [input().split() for _ in range(n)]
    alice_row, alice_col = None, None
    tea_bags = 0

    # Find Alice's initial position
    for i in range(n):
        for j in range(n):
            if field[i][j] == 'A':
                alice_row, alice_col = i, j
                break
        if alice_row is not None:
            break

    commands = iter(input().split())

    while True:
        command = next(commands, None)
        if command is None:
            break

        new_row, new_col = move_alice(field, alice_row, alice_col, command)

        if new_row is None or field[new_row][new_col] == 'R':
            break

        if field[new_row][new_col].isdigit():
            tea_bags += int(field[new_row][new_col])
            if tea_bags >= 10:
                break

        field[alice_row][alice_col] = '*'
        alice_row, alice_col = new_row, new_col

    if tea_bags >= 10:
        print("She did it! She went to the party.")
    else:
        print("Alice didn't make it to the tea party.")

    for row in field:
        print(' '.join(row))


if __name__ == "__main__":
    main()
