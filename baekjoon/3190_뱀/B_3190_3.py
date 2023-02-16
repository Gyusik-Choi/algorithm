from collections import deque


def move_snake():
    # 상, 우, 하, 좌
    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    # 현재 방향
    current_direction = 1
    # 게임 시간
    time = 0

    # 꼬리는 0번 인덱스, 머리는 마지막 인덱스
    deq = deque()
    deq.append([0, 0])

    while True:
        time += 1

        head_y = deq[-1][0] + y_value[current_direction]
        head_x = deq[-1][1] + x_value[current_direction]

        # 벽
        if 0 > head_y or head_y >= N or 0 > head_x or head_x >= N:
            break

        # 자기 자신
        # if board[head_y][head_x] 로 하면
        # board[head_y][head_x] 가 2인 경우도 if 문을 만족 하므로 주의
        if board[head_y][head_x] == 1:
            break

        # 사과 없음
        if not board[head_y][head_x]:
            tail_y = deq[0][0]
            tail_x = deq[0][1]

            board[tail_y][tail_x] = 0
            deq.popleft()

        # 이동
        board[head_y][head_x] = 1
        deq.append([head_y, head_x])

        # 방향 변환 여부
        if time in change_direction_info:
            direction = change_direction_info[time]

            # 왼쪽
            if direction == 'L':
                current_direction = (current_direction + 3) % 4
            # 오른쪽
            else:
                current_direction = (current_direction + 1) % 4

    return time


N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
change_direction_info = {}

for _ in range(L):
    X, C = input().split()
    change_direction_info[int(X)] = C

board = [[0] * N for _ in range(N)]
board[0][0] = 1

# 사과는 2로 표시
# 자기 자신은 1로 표시
for apple in apples:
    board[apple[0] - 1][apple[1] - 1] = 2

print(move_snake())
