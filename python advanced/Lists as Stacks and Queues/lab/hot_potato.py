from collections import deque

queue = deque(input().split(' '))
step = int(input())
while len(queue) != 1:
    i = 0
    while True:
        i += 1
        if i == step:
            print(f'Removed {queue.popleft()}')
            break
        else:
            queue.append(queue.popleft())

print(f'Last is {queue.popleft()}')


