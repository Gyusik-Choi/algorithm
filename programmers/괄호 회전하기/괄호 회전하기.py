from collections import deque


def is_right_parenthesis(s):
    stack = []

    for char in s:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
            continue

        if not stack:
            return False

        if ((char == ")" and stack[-1] == "(") or
                (char == "]" and stack[-1] == "[") or
                (char == "}" and stack[-1] == "{")):
            stack.pop()
            continue

        return False

    if stack:
        return False
    return True


def solution(s):
    deq = deque(s)
    length = len(s)
    cnt = 0

    for _ in range(length):
        front = deq.popleft()
        deq.append(front)

        if is_right_parenthesis(deq):
            cnt += 1

    return cnt


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
