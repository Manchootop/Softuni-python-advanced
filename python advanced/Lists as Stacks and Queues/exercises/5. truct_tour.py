# from collections import deque
#
# pumps_count = int(input())
# pump_stack = deque()
# distance_stack = deque()
#
# for _ in range(pumps_count):
#     pump_index, distance = input().split()
#     pump_stack.append(int(pump_index))
#     distance_stack.append(int(distance))
#
# min_index = 0
#
# while True:
#     petrol = pump_stack.popleft()
#     distance = distance_stack.popleft()
#
#     if min_index == len(pump_stack) - 1:
#         if petrol >= 0:
#             trip_done = True
#             break
#     if petrol >= distance:
#         break
#     min_index += 1
#
# print(min_index)

number_of_enters = int(input())
list_of_petrol = []
list_of_miles = []
our_petrol = 0
trip_done = False
currIndex = 0  # keep current index

for num in range(number_of_enters):
    our_enters = input().split(" ")
    amount_of_petrol = int(our_enters[0])
    amount_of_miles = int(our_enters[1])
    list_of_petrol.append(amount_of_petrol)
    list_of_miles.append(amount_of_miles)
while True:
    for sub_index in range(0, len(list_of_petrol)):
        petrol = list_of_petrol[sub_index]
        miles = list_of_miles[sub_index]
        our_petrol += petrol
        our_petrol -= miles
        if sub_index == len(list_of_petrol) - 1:
            if our_petrol >= 0:
                trip_done = True
                break
        if our_petrol < 0:
            our_petrol = 0
            list_of_petrol.append(list_of_petrol.pop(0))  # delete first element and add it at the end
            list_of_miles.append(list_of_miles.pop(0))  # delete first element and add it at the end
            break

    if trip_done:
        break
    currIndex = currIndex + 1  # increase the current index

print(currIndex)  # print the index
