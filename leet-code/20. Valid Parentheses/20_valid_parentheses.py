def is_valid(s: str):
    parentheses = dict()
    parentheses[')'] = '('
    parentheses['}'] = '{'
    parentheses[']'] = '['

    stack = []

    for char in s:
        if char not in parentheses:
            stack.append(char)
        else:
            if not stack:
                return False

            if stack[-1] != parentheses[char]:
                return False

            stack.pop()

    return not len(stack)


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
