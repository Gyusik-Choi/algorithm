def dfs(numbers, target, sums, cnt, answer):
    if cnt == len(numbers):
        if sums == target:
            answer += 1
        return answer

    answer = dfs(numbers, target, sums + numbers[cnt], cnt + 1, answer)
    answer = dfs(numbers, target, sums - numbers[cnt], cnt + 1, answer)
    return answer


def solution(numbers, target):
    return dfs(numbers, target, 0, 0, 0)


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))

# 숫자의 순서는 안 바뀐다
# 연산의 종류만 바뀐다
