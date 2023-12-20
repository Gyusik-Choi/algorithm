def solution(dirs):
    def get_key(idx1, idx2):
        return str(idx1) + " " + str(idx2)

    directions = dict()
    directions['U'] = [-1, 0]
    directions['R'] = [0, 1]
    directions['D'] = [1, 0]
    directions['L'] = [0, -1]

    size = 11
    visit = dict()
    y = 5
    x = 5
    cnt = 0

    for dir in dirs:
        y_value, x_value = directions[dir]
        y_idx = y_value + y
        x_idx = x_value + x

        if 0 > y_idx or y_idx >= size or 0 > x_idx or x_idx >= size:
            continue

        if get_key(y, x) in visit and [y_idx, x_idx] in visit[get_key(y, x)]:
            y, x = y_idx, x_idx
            continue

        if get_key(y_idx, x_idx) not in visit:
            visit[get_key(y_idx, x_idx)] = [[y, x]]
            cnt += 1
        else:
            if [y, x] not in visit[get_key(y_idx, x_idx)]:
                visit[get_key(y_idx, x_idx)].append([y, x])
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
