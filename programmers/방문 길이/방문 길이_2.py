from collections import defaultdict


def solution(dirs):
    def get_key(idx1, idx2):
        return str(idx1) + " " + str(idx2)

    def get_value(idx1, idx2):
        return get_key(idx1, idx2)

    directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    visit = defaultdict(list)
    y, x = 0, 0
    cnt = 0

    for dir in dirs:
        y_value, x_value = directions[dir]
        y_idx = y_value + y
        x_idx = x_value + x

        if -5 > y_idx or y_idx > 5 or -5 > x_idx or x_idx > 5:
            continue

        if get_key(y, x) in visit and get_value(y_idx, x_idx) in visit[get_key(y, x)]:
            y, x = y_idx, x_idx
            continue

        if get_key(y_idx, x_idx) in visit and get_value(y, x) in visit[get_key(y_idx, x_idx)]:
            y, x = y_idx, x_idx
            continue

        visit[get_key(y_idx, x_idx)].append(get_value(y, x))
        cnt += 1
        y, x = y_idx, x_idx

    return cnt


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
# 반례
# https://school.programmers.co.kr/questions/57398
print(solution("UDLRDURL"))
# 참고
# https://school.programmers.co.kr/questions/12506
# https://school.programmers.co.kr/questions/12535
