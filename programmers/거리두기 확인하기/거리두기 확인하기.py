from collections import deque


def solution(places):
    def get_distance(start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def is_safe_distance(start_distance, start, end):
        return start_distance + get_distance(start, end) >= 3

    def is_safe(room, start, end):
        distance = get_distance(start, end)

        if distance == 1 and room[end[0]][end[1]] == 'P':
            return False

        if distance == 2 and room[start[0]][start[1]] == 'O':
            return False

        return True

    def bfs(room, go):
        deq = deque([go])
        visited = [[False] * 5 for _ in range(5)]
        visited[go[1]][go[2]] = True
        y_value = [-1, -1, 0, 1, 1, 1, 0, -1]
        x_value = [0, 1, 1, 1, 0, -1, -1, -1]

        while deq:
            dist, y, x = deq.popleft()

            for m in range(8):
                y_idx, x_idx = y + y_value[m], x + x_value[m]

                if 0 > y_idx or y_idx >= 5 or 0 > x_idx or x_idx >= 5:
                    continue

                if visited[y_idx][x_idx]:
                    continue

                if is_safe_distance(dist, [y, x], [y_idx, x_idx]):
                    continue

                if room[y_idx][x_idx] == 'X':
                    continue

                if not is_safe(room, [y, x], [y_idx, x_idx]):
                    return False

                # 아래 조건문 없이 실행하면 오답이 나온다
                # 만약 아래 조건문이 없고
                # "XXXXX"
                # "XXXXX"
                # "XXXXX"
                # "XXXXP"
                # "XXXPO"
                # 위와 같은 places 가 주어지면
                # (3, 4) 의 P 가 for 문을 돌면서
                # deq 에 (4, 3) 의 P 를 넣고
                # visited 에 방문 처리를 한다
                # 이후
                # deq 에서 (4, 4) 의 O 가 꺼내지고
                # (4, 4) 의 O 가 for 문을 돌면서
                # (4, 3) 의 P 가 is_safe 함수에 의해서
                # return False 가 되길 기대 하지만
                # 실제로는 (4, 3) 의 P 가 이미 방문 처리 돼서
                # if visited[y_idx][x_idx] 에 의해 continue 되어서
                # is_safe 함수를 타지 못한다
                if room[y_idx][x_idx] == 'O':
                    deq.append([dist + get_distance([y, x], [y_idx, x_idx]), y_idx, x_idx])
                    visited[y_idx][x_idx] = True

        return True

    answer = []

    for k, place in enumerate(places):
        for i, p in enumerate(place):
            place[i] = list(p)

    for k, place in enumerate(places):
        is_keep_distance = True
        for i, p in enumerate(place):
            for j, spot in enumerate(p):
                if spot == 'P':
                    if not bfs(place, [0, i, j]):
                        is_keep_distance = False
                        break
            if not is_keep_distance:
                break
        answer.append(1 if is_keep_distance else 0)

    return answer


print(solution([
    # ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    # ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    # ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    # ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    # ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]))
