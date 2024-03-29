from collections import deque

boxes = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

presents = {
    150: 'Doll',
    250: 'Wooden train',
    350: 'Teddy bear',
    400: 'Bicycle',
}

crafted_presents = {}

while boxes and magic_values:
    box = boxes.pop()
    magic_value = magic_values.popleft()
    result = box * magic_value

    if box == 0 and magic_value == 0:
        continue

    if box == 0:
        magic_values.appendleft(magic_value)
        continue

    if magic_value == 0:
        boxes.append(box)
        continue

    if result < 0:
        boxes.append(box + magic_value)
    elif result in presents:
        present = presents[result]
        if present in crafted_presents:
            crafted_presents[present] += 1
        else:
            crafted_presents[present] = 1
    else:
        boxes.append(box + 15)


is_done = ('Doll' in crafted_presents and 'Wooden train' in crafted_presents) or \
          ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents)

if is_done:
    print('THe presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')


if boxes:
    print(f"Materials left: {', '.join(reversed([str(x) for x in boxes]))}")

if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for present, count in sorted(crafted_presents.items()):
    print(f'{present}: {count}')