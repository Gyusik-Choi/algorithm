def solution(x, n):
    answer = [x]

    for _ in range(n - 1):
        answer.append(answer[-1] + x)

    return answer


print(solution(2, 5))
print(solution(-4, 2))
