def solution(numbers, target):
    answer = 0

    def dfs(cnt, cnt_limit, sums):
        nonlocal answer

        if cnt == cnt_limit:
            if sums == target:
                answer += 1
            return

        for i in range(2):
            if i == 0:
                sums += numbers[cnt]
                dfs(cnt + 1, cnt_limit, sums)
                sums -= numbers[cnt]
            else:
                sums -= numbers[cnt]
                dfs(cnt + 1, cnt_limit, sums)
                sums += numbers[cnt]

    dfs(0, len(numbers), 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))

# 숫자의 순서는 안 바뀐다
# 연산의 종류만 바뀐다
