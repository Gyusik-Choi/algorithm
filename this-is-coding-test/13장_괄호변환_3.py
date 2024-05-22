def change_u(u):
    u = list(u)
    u.pop(0)
    u.pop()

    for i in range(len(u)):
        if u[i] == ")":
            u[i] = "("
        else:
            u[i] = ")"

    return "".join(u)


# def is_right(w):
#     if w[0] == ")":
#         return False
#
#     stack = [w[0]]
#
#     for i in range(1, len(w)):
#         char = w[i]
#
#         if not stack:
#             if char == ")":
#                 return False
#             else:
#                 stack.append(char)
#         else:
#             if stack[-1] != char:
#                 stack.pop()
#             else:
#                 stack.append(char)
#
#     if not stack:
#         return True
#
#     return False

def is_right(w):
    stack = []

    for idx, char in enumerate(w):
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                stack.append(char)
            else:
                stack.pop()

    if not stack:
        return True

    return False


def divide(w):
    u = ""
    v = ""

    left_count = 0
    right_count = 0

    last_idx = 0
    for i in range(len(w)):
        char = w[i]
        u += char

        if char == ")":
            right_count += 1
        else:
            left_count += 1

        if left_count == right_count:
            last_idx = i + 1
            break

    for i in range(last_idx, len(w)):
        char = w[i]
        v += char

    return [u, v]


def solution(p):
    if not len(p):
        return ""

    u, v = divide(p)

    if is_right(u):
        return u + solution(v)

    characters = "("
    characters += solution(v)
    characters += ")"
    characters += change_u(u)
    return characters


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
