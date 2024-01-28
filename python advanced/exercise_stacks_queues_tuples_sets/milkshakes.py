from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk = deque()
[milk.append(int(x)) for x in input().split(', ')]

milkshakes = 0

while not milkshakes == 5 and milk and chocolate:
    curr_chocolate = chocolate.pop()
    curr_milk = milk.popleft()

    if curr_chocolate <= 0 and curr_milk <= 0:
        break
    elif curr_chocolate <= 0:
        milk.appendleft(curr_milk)
    elif curr_milk <= 0:
        chocolate.append(curr_chocolate)
    elif curr_chocolate == curr_milk:
        milkshakes += 1
    else:
        curr_chocolate -= 5
        chocolate.append(curr_chocolate)
        milk.append(curr_milk)

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolate:
    choco_str = ", ".join([str(x) for x in chocolate])
    print(f'Chocolate: {choco_str}')
else:
    print("Chocolate: empty")

if milk:
    milk_str = ", ".join([str(x) for x in milk])
    print(f'Milk: {milk_str}')
else:
    print("Milk: empty")

