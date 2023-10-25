text = input()
text = list(text)
stack = [text.pop() for _ in range(len(text))]

print("".join(stack))

