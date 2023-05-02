def change_direction(u):
    new_u = ''

    for char in u:
        if char == "(":
            new_u += ")"
        else:
            new_u += "("

    return new_u


def is_right_string(u):
    stack = []

    for idx, char in enumerate(u):
        if char == ")":
            if not stack:
                return False

            stack.pop()
        else:
            stack.append(char)

    if stack:
        return False

    return True

def get_balanced_string(w):
    front = 0
    back = 0

    u = ''
    v = ''

    for idx, char in enumerate(w):
        if char == "(":
            front += 1
        else:
            back += 1

        u += char

        if front and back and front == back:
            v += w[idx + 1:]
            break

    return [u, v]


def solution(p):
    if not p:
        return ""

    u, v = get_balanced_string(p)

    if is_right_string(u):
        u += solution(v)
        return u

    empty_string = "("
    empty_string += solution(v)
    empty_string += ")"
    empty_string += change_direction(u[1:-1])

    return empty_string


# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))
