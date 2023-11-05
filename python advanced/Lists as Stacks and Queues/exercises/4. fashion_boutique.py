stack = []
[stack.append(int(box)) for box in input().split()]
rack_quantity = int(input())
sum = 0
racks_req = 0
while stack:

    curr = stack.pop()
    if curr + sum > rack_quantity:
        sum = curr
        racks_req += 1
    else:
        sum += curr

print(racks_req + (1 if sum != 0 else 0))
