def solution(n, stages):
    answer = []
    stages.sort()

    target = 1
    start_idx = 0
    total_players = len(stages)

    while target <= n:
        cnt = 0

        for idx in range(start_idx, len(stages)):
            if target == stages[idx]:
                start_idx = idx
                cnt += 1

        if not total_players:
            for _ in range(n - target + 1):
                answer.append([0, target])
                break
        else:
            fail_rate = cnt / total_players
            answer.append([fail_rate, target])
            total_players -= cnt

        target += 1

    answer.sort(key=lambda x: (-x[0], x[1]))
    answer = list(map(lambda x: x.pop(1), answer))
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(5, [1, 1, 1, 1, 1]))
