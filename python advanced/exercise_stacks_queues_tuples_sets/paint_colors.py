from collections import deque

main_colors = {'red', 'yellow', 'blue'}
secondary_colors = {'orange', 'purple', 'green'}
# check named tuple

substrings = deque(input().split())
collected_colors = []
while substrings:
    left = substrings.popleft()
    right = substrings.pop() if substrings else ''
    color = left + right
    if color in main_colors or color in secondary_colors:
        collected_colors.append(color)
        continue
    color = right + left
    if color in main_colors or color in secondary_colors:
        collected_colors.append(color)
    else:
        pass
