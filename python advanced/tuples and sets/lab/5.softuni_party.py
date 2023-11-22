guests_count = int(input())
guests_set = set()
vip_guests = set()

for i in range(guests_count):
    guest = input()
    if guest.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
        vip_guests.add(guest)
    else:
        guests_set.add(guest)


command = input()

while command != "END":
    if command in guests_set:
        guests_set.remove(command)
    elif command in vip_guests:
        vip_guests.remove(command)
    command = input()

print(len(guests_set) + len(vip_guests))
[print(guest) for guest in sorted(vip_guests)]
# [print(guest) for guest in sorted(guests_set)]

for guest in guests_set:
    print(guest)



