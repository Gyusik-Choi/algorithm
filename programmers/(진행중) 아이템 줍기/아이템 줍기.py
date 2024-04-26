from collections import deque


def solution(rectangle, character_x, character_y, item_x, item_y):
    def mark_rectangle():
        for r in rectangle:
            x_1, y_1, x_2, y_2 = r
            for i in range(y_1, y_2 + 1):
                for j in range(x_1, x_2 + 1):
                    matrix[i][j] = 1

    def is_circumference(coordinate):
        y, x = coordinate
        y_value = [-1, -1, 0, 1, 1, 1, 0, -1]
        x_value = [0, 1, 1, 1, 0, -1, -1, -1]

        for i in range(8):
            y_idx, x_idx = y + y_value[i], x + x_value[i]

            if y_idx <= 0 or y_idx >= 51 or x_idx <= 0 or x_idx >= 51:
                return True

            if not matrix[y_idx][x_idx]:
                return True

        return False

    def bfs():
        y_value = [-1, -1, 0, 1, 1, 1, 0, -1]
        x_value = [0, 1, 1, 1, 0, -1, -1, -1]

        visit = [[0] * 51 for _ in range(51)]
        visit[character_y][character_x] = 1
        deq = deque([[character_y, character_x, 0]])

        while deq:
            y, x, cnt = deq.popleft()

            if y == item_y and x == item_x:
                return cnt + 1

            for i in range(8):
                y_idx, x_idx = y + y_value[i], x + x_value[i]

                # < 0 이 아니라 <= 0 에 주의
                if y_idx <= 0 or y_idx >= 51 or x_idx <= 0 or x_idx >= 51:
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
    # 인덱스로 좌표를 그대로 사용하기 위해
    # 50이 아닌 51로 크기 설정함
    matrix = [[0] * 51 for _ in range(51)]
    mark_rectangle()
    answer = bfs()
    return answer


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
# print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
# print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
# print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
# print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))

# 이동할 수 있는 위치 기준
# ->
# 1
# 방문 X
# 둘러싼 8방향 중 하나라도 False or 가장 자리
