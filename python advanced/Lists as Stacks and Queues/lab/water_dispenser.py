from collections import deque

quantity = int(input())

queue = deque()
name = input()
while name != 'Start':
    queue.append(name)
    name = input()

command = input()

while command != 'End':
    if 'refill' in command:
        quantity += int(command.split()[1])
    else:
        liters = int(command)
        if liters <= quantity:
            quantity -= liters
            print(f'{queue.popleft()} got water')
        else:
            print(f'{queue.popleft()} must wait')
    command = input()
print(f'{quantity} liters left')




