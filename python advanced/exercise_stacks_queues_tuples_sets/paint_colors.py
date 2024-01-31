from collections import deque

main_colors = {'red', 'yellow', 'blue'}
secondary_colors = {'orange'', ''
# check named tuple

substrings = deque(input().split())

while substrings:
    left = substrings.popleft()
    right = substrings.pop() if substrings else ''

