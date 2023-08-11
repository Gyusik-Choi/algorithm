def solution(ingredient):
    stack = []
    cnt = 0

    for i in ingredient:
        stack.append(i)

        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for _ in range(4):
                stack.pop()

    return cnt


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
