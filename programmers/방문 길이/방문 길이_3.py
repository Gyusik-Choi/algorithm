def solution(dirs):
    directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    visit = set()
    y, x = 0, 0

    for direction in dirs:
        y_value, x_value = directions[direction]
        y_idx, x_idx = y_value + y, x_value + x

        if -5 > y_idx or y_idx > 5 or -5 > x_idx or x_idx > 5:
            continue

        visit.add((y, x, y_idx, x_idx))
        visit.add((y_idx, x_idx, y, x))
        y, x = y_idx, x_idx

    return len(visit) // 2


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
# 반례
# https://school.programmers.co.kr/questions/57398
print(solution("UDLRDURL"))
# 참고
# https://school.programmers.co.kr/questions/12506
# https://school.programmers.co.kr/questions/12535
# https://school.programmers.co.kr/learn/courses/30/lessons/49994/solution_groups?language=python3

