rows, columns = input().split(', ')
array = []
sum = 0

for row in range(int(rows)):
    nums = input().split(', ')
    array.append(nums)
    for column in range(int(columns)):
        sum += int(nums[column])

print(sum)
print(array)