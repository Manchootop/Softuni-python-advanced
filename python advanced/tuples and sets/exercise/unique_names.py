n = int(input())

names = set()
for i in range(n):
    names.add(input())


[print(x) for x in names]