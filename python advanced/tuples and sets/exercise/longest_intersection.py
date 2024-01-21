n = int(input())

longest_intersection = set()
for i in range(n):
    first, second = [x.split(',') for x in input().split('-')]
    first_start, first_end = first
    second_start, second_end = second
    first_range = set(range(first_start, first_end + 1))
    second_range = set(range(second_start, second_end + 1))
    current_intersection = first_range.intersection(second_range)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f'Longest intersection is {", ".join([str(x) for x in longest_intersection])} with length: {len(longest_intersection)}')