def solution(s):
    stack = []

    for idx, char in enumerate(s):
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    return True


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
