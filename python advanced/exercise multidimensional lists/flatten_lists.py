def flatten_lists(input_string):
    lists = input_string.strip().split('|')
    flattened_list = []
    for sublist in reversed(lists):
        numbers = sublist.strip().split()
        flattened_list.extend(numbers)
    return ' '.join(flattened_list)

# Test cases
inputs = [
    "1 2 3 |4 5 6 | 7 88 7 88",
    "7 | 4 5|1 0| 2 5 |3 3",
    "1| 4 5 6 7 | 8 9 8 9"
]

for input_str in inputs:
    output = flatten_lists(input_str)
    print(f"Input: {input_str}")
    print(f"Output: {output}")
