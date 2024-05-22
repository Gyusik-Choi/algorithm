def solution(n, stages):
    stages.sort()

    fail_rate = []

    total = len(stages)
    idx = 0

    for cur_stage in range(1, n + 1):
        cnt = 0

        for i in range(idx, len(stages)):
            idx = i

            if stages[i] != cur_stage:
                break

            cnt += 1

        if cnt:
            fail_rate.append([cnt / total, cur_stage])
            total -= cnt
        else:
            fail_rate.append([0, cur_stage])


    return list(map(lambda x: x[1], sorted(fail_rate, key=lambda x: (-x[0], x[1]))))


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(3, [1, 1, 1]))
