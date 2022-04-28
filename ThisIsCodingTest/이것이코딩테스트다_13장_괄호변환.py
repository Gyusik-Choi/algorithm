# 올바른 괄호 문자열 판단
def is_right(u):
    stack = []
    for item in u:
        if item == "(":
            stack.append(item)
        else:
            if not stack:
                return False
            else:
                stack.pop()

    if stack:
        return False
    return True


# 균형 잡힌 문자열 형태로 분리
def u_and_v(p):
    p = list(p)
    left_cnt = 0
    right_cnt = 0
    u = ""
    v = ""
    for i, item in enumerate(p):
        u += item

        if item == "(":
            left_cnt += 1
        else:
            right_cnt += 1

        if left_cnt == right_cnt:
            v = ''.join(p[i + 1:])
            break

    return [u, v]


def solution(p):
    if not p:
        return p

    u, v = u_and_v(p)

    if is_right(u):
        return u + solution(v)

    else:
        empty = "("
        empty += solution(v)
        empty += ")"

        u = list(u)
        u.pop(0)
        u.pop()

        for i, item in enumerate(u):
            if item == "(":
                u[i] = ")"
            else:
                u[i] = "("

        u = ''.join(u)
        empty += u
        return empty


# print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
# print(solution("))(("))
# => ()()
# print(solution("))))(((("))
# => ()((()))
# print(solution("))()(("))
# => ()()()
