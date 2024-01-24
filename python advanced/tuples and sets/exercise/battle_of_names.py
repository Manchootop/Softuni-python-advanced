n = int(input())
odd_set = set()
even_set = set()

for row in range(1, n + 1):
    ascii_sum = 0
    for ch in input():
        ascii_sum += int(ord(ch))

    ascii_sum /= row

    ascii_sum = int(ascii_sum)


    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if odd_sum == even_sum:
    print(odd_set.union(even_set))
elif even_sum > odd_sum:
    print(even_set.symmetric_difference(odd_set))
elif odd_sum > even_sum:
    # [print(x, end=", ") for x in odd_set]
    print(", ".join([str(x) for x in odd_set]))