"""
You have an empty stack. You will receive an integer – N. On the next N lines you will receive queries. Each query is one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from the top to the bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"

"""
n = int(input())
stack = []

for command in range(n):
    str = input().split()

    if '1' in str:
        stack.append(int(str[1]))
    elif str[0] == '2':
        stack.pop()
    elif str[0] == '3':
        print(max(stack))
    elif str[0] == '4':
        print(min(stack))

while stack:
    if len(stack) == 1:
        print(stack.pop(), end=' ')
    else:
        print(stack.pop(), end=', ')

