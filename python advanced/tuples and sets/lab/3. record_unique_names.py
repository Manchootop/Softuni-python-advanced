n = int(input())
unique_names = set()
for i in range(n):
    unique_names.add(input())

[print(person) for person in unique_names]