parentheses_dict = {')': '(', '}': '{', ']': '['}
opening_ones = '{[('
str = input()
opening_parentheses = []
balanced = True
for ch in str:
    if ch in opening_ones:
        opening_parentheses.append(ch)
    else:
        if not opening_parentheses or parentheses_dict[ch] != opening_parentheses.pop():
            balanced = False
            break
if balanced and not opening_parentheses:
    print('YES')
else:
    print('NO')
