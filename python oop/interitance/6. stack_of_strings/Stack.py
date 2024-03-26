class Stack():
    def __init__(self, data: []):
        self.data = data

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def __str__(self):
        return ' '.join(map(str, self.data))


stack = Stack(['1', '2', '3', '4', '5', '6'])
print(stack.push('7'))
print(stack)
print(stack.is_empty())
print(stack.pop())
print(stack)

