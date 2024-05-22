def solution(n, stages):
    users = [0] * (n + 1)

    for idx, stage in enumerate(stages):
        if stage > n:
            continue

        users[stage] += 1

    total_users = len(stages)
    fail_rate = []

    for i in range(1, len(users)):
        user_cnt = users[i]

        if not user_cnt:
            fail_rate.append([0, i])
        else:
            fail_rate.append([user_cnt / total_users, i])
            total_users -= user_cnt

    return list(map(lambda x: x[1], sorted(fail_rate, key=lambda x: (-x[0], x[1]))))


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
