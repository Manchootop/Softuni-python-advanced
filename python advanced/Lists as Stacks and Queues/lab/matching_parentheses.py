# math_expression = input()
# opening_parenthesis_stack = []
# closing_parenthesis_stack = []
#
# for ch in math_expression:
#     if ch == '(':
#         opening_parenthesis_stack.append(math_expression.index(ch))
#     if ch == ')':
#         closing_parenthesis_stack.append(math_expression.index(ch))
#
# for _ in range(len(opening_parenthesis_stack)):
#     start_index = opening_parenthesis_stack.pop()
#     end_index = closing_parenthesis_stack.pop()
#     print(math_expression[start_index: end_index])


text = input()
parentheses = []

for i in range(len(text)):
    if text[i] == '(':
        parentheses.append(i)
    elif text[i] == ')':
        start_index = parentheses.pop()
        print(text[start_index: i + 1])