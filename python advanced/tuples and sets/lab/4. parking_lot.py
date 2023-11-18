commands = int(input())
lot = set()

for _ in range(commands):
    line = input().split(', ')
    direction, car_id = tuple(line)
    if direction == 'OUT':
        lot.remove(car_id)
    elif direction == 'IN':
        lot.add(car_id)

if lot:
    [print(_id) for _id in lot]
else:
    print('Parking Lot is Empty')