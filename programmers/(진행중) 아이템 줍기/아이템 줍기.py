from collections import deque


def solution(rectangle, character_x, character_y, item_x, item_y):
    def mark_rectangle():
        for rec in rectangle:
            x_1, y_1, x_2, y_2 = rec
            for i in range(y_1, y_2 + 1):
                for j in range(x_1, x_2 + 1):
                    matrix[i][j] = 1

    def is_circumference(coordinate):
        y, x = coordinate
        y_value = [-1, -1, 0, 1, 1, 1, 0, -1]
        x_value = [0, 1, 1, 1, 0, -1, -1, -1]

        for i in range(8):
            y_idx, x_idx = y + y_value[i], x + x_value[i]

            if y_idx <= 0 or y_idx >= 101 or x_idx <= 0 or x_idx >= 101:
                return True

            if not matrix[y_idx][x_idx]:
                return True

        return False

    def bfs():
        # 8방향이 아닌 4방향 이동
        # 1 0 0 0
        # 1 1 0 0
        # 0 0 0 0
        # 8방향으로 가면 안 된다
        # (0,0) 에서 (1,1) 로 가려면
        # 중간에 (1,0) 을 거쳐서 가야 하는데
        # 8방향으로 가면
        # (0,0) 에서 (1,1) 로 바로 이동할 수 있게 된다
        # y_value = [-1, -1, 0, 1, 1, 1, 0, -1]
        # x_value = [0, 1, 1, 1, 0, -1, -1, -1]
        y_value = [-1, 0, 1, 0]
        x_value = [0, 1, 0, -1]

        visit = [[0] * 101 for _ in range(101)]
        visit[character_y][character_x] = 1
        deq = deque([[character_y, character_x, 0]])

        while deq:
            y, x, cnt = deq.popleft()

            if y == item_y and x == item_x:
                return cnt // 2

            # for i in range(8):
            for i in range(4):
                y_idx, x_idx = y + y_value[i], x + x_value[i]

                # < 0 이 아니라 <= 0 에 주의
                if y_idx <= 0 or y_idx >= 101 or x_idx <= 0 or x_idx >= 101:
                    continue

                if visit[y_idx][x_idx]:
                    continue

                if not matrix[y_idx][x_idx]:
                    continue

                if not is_circumference([y_idx, x_idx]):
                    continue

                visit[y_idx][x_idx] = 1
                deq.append([y_idx, x_idx, cnt + 1])

    # 1부터 50까지로 좌표가 주어져서
    # 인덱스로 좌표를 그대로 활용함
    # 단, 모든 좌표를 2배씩 증가한다
    #
    # 1 0 0 0
    # 1 1 1 0
    # 0 1 1 0
    # 문제에서 요구한대로 테두리를 따라
    # (0,0) 에서 (2,1) 로 가려면
    # (0,0) -> (1,0) -> (1,1) -> (1,2) -> (2,2) -> (2,1) 로 가야 하는데
    # 배열을 기준으로 BFS 를 하면
    # (0,0) -> (1,0) -> (1,1) -> (2,1) 로 가게 된다
    # 즉 (1,1) 에서 (2,1) 로 길이 이어진 것처럼 배열에는 나오지만
    # 테두리는 실제로 (1,1) 에서 (2,1) 로 이어지지 않았다
    # 따라서 BFS 탐색에서 이어지지 않은 길을 명확하게 나타낼 수 있도록
    # 각 좌표를 2배씩 늘려서 배치한 후에
    # cnt 에서 2를 나눈 몫을 리턴한다
    for idx, r in enumerate(rectangle):
        rectangle[idx] = list(map(lambda x: x * 2, r))
    character_x *= 2
    character_y *= 2
    item_x *= 2
    item_y *= 2
    matrix = [[0] * 101 for _ in range(101)]
    mark_rectangle()
    answer = bfs()
    return answer


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))

# 이동할 수 있는 위치 기준
# ->
# 1
# 방문 X
# 둘러싼 8방향 중 하나라도 False or 가장 자리
