def parse_matrix(matrix):
    return [list(row.split()) for row in matrix]

def print_targets_hit(targets_hit):
    for target in targets_hit:
        print(f"[{target[0]}, {target[1]}]")

def validate_position(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def shotgun_training(matrix, commands):
    targets_hit = []
    directions = {'right': (0, 1), 'left': (0, -1), 'up': (-1, 0), 'down': (1, 0)}

    # Parse the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Find the position of 'A'
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'A':
                current_row = r
                current_col = c

    # Execute commands
    for command in commands:
        parts = command.split()
        action = parts[0]
        direction = parts[1]
        if action == 'move':
            steps = int(parts[2])
            dr, dc = directions[direction]
            new_row = current_row + steps * dr
            new_col = current_col + steps * dc
            if validate_position(new_row, new_col, rows, cols) and matrix[new_row][new_col] == '.':
                current_row = new_row
                current_col = new_col
        elif action == 'shoot':
            dr, dc = directions[direction]
            new_row = current_row
            new_col = current_col
            while validate_position(new_row, new_col, rows, cols):
                if matrix[new_row][new_col] == 'x':
                    targets_hit.append((new_row, new_col))
                    matrix[new_row][new_col] = '.'
                    break
                new_row += dr
                new_col += dc

    # Check if all targets were hit
    all_targets_hit = all(matrix[row][col] != 'x' for row, col in targets_hit)
    if all_targets_hit:
        print(f"Training completed! All {len(targets_hit)} targets hit.")
    else:
        print(f"Training not completed! {sum(row.count('x') for row in matrix)} targets left.")
    print_targets_hit(targets_hit)

# Example usage
matrix = [
    ". A . 1 1 . .",
    "9 . . . 6 . 5",
    ". 6 . R . . .",
    ". 3 . . 1 . .",
    ". . . 2 . . 2"
]
commands = [
    "left",
    "down",
    "down",
    "right"
]

shotgun_training(parse_matrix(matrix), commands)
