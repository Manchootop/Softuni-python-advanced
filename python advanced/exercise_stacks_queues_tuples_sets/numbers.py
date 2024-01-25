first_set = set()
first_set.update(input().split())
second_set = set()
second_set.update(input().split())


n = int(input())

for _ in range(n):
    txt = input().split(' ')
    first_command = txt[0]
    second_command = txt[1]

    if first_command == 'Add':
        if second_command == 'First':
            first_set.add(txt[:2])
        else:
            second_set.add(txt[:2])
    elif first_command == 'Remove':
        pass
