def find_best_direction(field_size, field):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # (row_increment, col_increment) for each direction
    max_eggs = 0
    best_direction = None
    best_positions = []

    for d_row, d_col in directions:
        row, col = None, None
        eggs_collected = 0
        positions = []

        # Find bunny position
        for i in range(field_size):
            for j in range(field_size):
                if field[i][j] == 'B':
                    row, col = i, j
                    break
            if row is not None:
                break

        # Move in the current direction until encountering a trap or reaching the boundary
        while 0 <= row < field_size and 0 <= col < field_size:
            if field[row][col] == 'X':  # Trap encountered, stop moving in this direction
                break
            elif field[row][col] == 'E':  # Egg collected
                eggs_collected += 1
                positions.append((row, col))

            # Move to the next position in the current direction
            row += d_row
            col += d_col

        # Update max_eggs and best_direction if eggs_collected in this direction is greater
        if eggs_collected > max_eggs:
            max_eggs = eggs_collected
            best_direction = (d_row, d_col)
            best_positions = positions

    # Convert the direction tuple to a lowercase string
    if best_direction == (0, 1):
        direction_str = "right"
    elif best_direction == (0, -1):
        direction_str = "left"
    elif best_direction == (1, 0):
        direction_str = "down"
    elif best_direction == (-1, 0):
        direction_str = "up"
    else:
        direction_str = "stay"

    return direction_str, best_positions, max_eggs

# Example usage:
field_size = int(input())
field = [input().split() for _ in range(field_size)]

direction, positions, total_eggs = find_best_direction(field_size, field)
print(direction)
print(positions)
print(total_eggs)
