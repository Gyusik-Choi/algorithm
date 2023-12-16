def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    # 역순으로 탐색
    for i in range(len(numbers) - 1, -1, -1):
        while stack:
            if stack[-1] > numbers[i]:
                answer[i] = stack[-1]
                break
            else:
                stack.pop()

        if not stack:
            answer[i] = -1
        stack.append(numbers[i])

    return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))

# 참고
# https://jaewoo2233.tistory.com/89
# https://sasca37.tistory.com/306
