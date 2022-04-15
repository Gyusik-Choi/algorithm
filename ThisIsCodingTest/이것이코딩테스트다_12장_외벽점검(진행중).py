import copy


def find_next_t_counter_clockwise(wall, last_idx):
    idx = 1

    while idx < len(wall):
        i = (last_idx - idx) % len(wall)

        if wall[i][1] == 0:
            return i

        idx += 1


def find_next_t_clockwise(wall, last_idx):
    idx = 1

    while idx < len(wall):
        i = (last_idx + idx) % len(wall)

        if wall[i][1] == 0:
            return i

        idx += 1


def is_all_checked(wall):
    for w in wall:
        if w[0] == 1 and w[1] == 0:
            return False

    return True


def counter_clockwise(wall, w, dist):
    temp_cnt = 0
    temp_wall = copy.deepcopy(wall)
    next_w = w
    last_idx = 0

    # 지점에서 하나 잡고 점검하고
    # 완료 안 됐으면
    # 다음 지점을 찾고
    # 그 지점에서 다시 점검
    # 이를 완전히 점검하거나 dist 를 다 돌때까지 완료

    for d in dist:
        temp_cnt += 1
        for i in range(d + 1):
            idx = (next_w - i) % len(wall)
            temp_wall[idx][1] = 1
            last_idx = idx

            if is_all_checked(temp_wall):
                return temp_cnt

        next_w = find_next_t_counter_clockwise(wall, last_idx)

    return -1


def clockwise(wall, w, dist):
    temp_cnt = 0
    temp_wall = copy.deepcopy(wall)
    next_w = w
    last_idx = 0

    # 지점에서 하나 잡고 점검하고
    # 완료 안 됐으면
    # 다음 지점을 찾고
    # 그 지점에서 다시 점검
    # 이를 완전히 점검하거나 dist 를 다 돌때까지 완료

    for d in dist:
        temp_cnt += 1
        for i in range(d + 1):
            idx = (next_w + i) % len(wall)
            temp_wall[idx][1] = 1
            last_idx = idx

            if is_all_checked(temp_wall):
                return temp_cnt

        next_w = find_next_t_clockwise(wall, last_idx)

    return -1


def solution(n, weak, dist):
    # 취약, 점검
    wall = [[0, 0] for _ in range(n)]
    for w in weak:
        wall[w][0] = 1

    dist.sort(reverse=True)

    answer = []

    for w in weak:
        clockwise_cnt = clockwise(wall, w, dist)
        answer.append(clockwise_cnt)

        counter_clockwise_cnt = counter_clockwise(wall, w, dist)
        answer.append(counter_clockwise_cnt)

    min_cnt = float('inf')
    for a in answer:
        if a > 0:
            min_cnt = min(min_cnt, a)

    if min_cnt == float('inf'):
        return -1
    return min_cnt


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
