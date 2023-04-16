def get_combinations(combination, cnt, cnt_limit, idx, idx_limit):
    global balls_cnt

    if cnt == cnt_limit:
        # 문제에 맞춰서
        # 구체적 경우의 수를 구하지 않고 갯수만 구한다
        balls_cnt += 1
        return

    for i in range(idx, idx_limit):
        # combination 배열에 볼링공 있고 마지막 볼링공 번호가 현재 볼링공 번호와 같은 경우 제외
        if combination and combination[-1] == balls[i]:
            continue

        combination.append(balls[i])
        get_combinations(combination, cnt + 1, cnt_limit, i + 1, idx_limit)
        combination.pop()


N, M = map(int, input().split())
balls = list(map(int, input().split()))
balls.sort()

balls_cnt = 0
get_combinations([], 0, 2, 0, N)
print(balls_cnt)
