from collections import deque


def bfs(y, x, b):
    y_location = [-1, 0, 1, 0]
    x_location = [0, 1, 0, -1]
    deq = deque()
    deq.append([y, x, b])
    while deq:
        y_axis, x_axis, is_break = deq.popleft()
        if y_axis == N - 1 and x_axis == M - 1:
            return visited[y_axis][x_axis][is_break]

        for i in range(4):
            y_idx = y_axis + y_location[i]
            x_idx = x_axis + x_location[i]
            if 0 <= y_idx < N and 0 <= x_idx < M:
                if not visited[y_idx][x_idx][is_break]:
                    # 여기서 목적지에 도착했는제 체크해주면
                    # 1 1
                    # 0
                    # 이것을 처리하지 못한다
                    # 여기가 아니라 위에서 처리하게 되면 처리할 수 있다
                    # 왜냐면 여기는 기존 지점에서 벗어나서 이동 가능한 지점을 체크하기 때문에
                    # 출발지와 목적지가 같은 경우를 체크할 수 없다
                    # if y_idx == N - 1 and x_idx == M - 1:
                    #     return visited[y_axis][x_axis][is_break] + 1

                    if maps[y_idx][x_idx] == 0:
                        visited[y_idx][x_idx][is_break] = visited[y_axis][x_axis][is_break] + 1
                        deq.append([y_idx, x_idx, is_break])
                    elif maps[y_idx][x_idx] == 1 and is_break == 0:
                        visited[y_idx][x_idx][is_break + 1] = visited[y_axis][x_axis][is_break] + 1
                        deq.append([y_idx, x_idx, is_break + 1])

    return -1


N, M = map(int, input().split())
maps = []
for _ in range(N):
    numbers = list(map(int, input()))
    maps.append(numbers)

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
print(bfs(0, 0, 0))

# 정말 이해하기 어려운 문제였다
# 문제의 풀이 개념은 이해했으나 다른 분들의 코드를 이해하는게 쉽지 않았다
# 특히 방문 처리를 하는 배열을 3차원으로 주로 만들어서(2차원 2개를 만드는 방법도 있다)(y x z 라고 하면 z 의 인덱스 크기를 2로 한다) 진행하는 부분이 어려웠다
# 아예 0과 1을 구분해서 진행하는 것인데 처음에는 오해해서 하나는 벽을 부쉈는지 안부쉈는지를 체크하고 나머지 하나는 이동한 칸을 세는 것으로 착각했다
# 0과 1을 구분해서 진행하는 이유는 1에서 0으로는 갈수가 없다
# 한번 부수면 더 부술 수 없고 그리고 안부수고 온게 최단거리인지 부수고 온게 최단거리인지 제대로 파악하기 위해 구분해서 진행한다
# https://kscodebase.tistory.com/66
# https://yuuj.tistory.com/94

# 이전 의문사항...
# 전역에 방문체크를 두면 이후에 최단으로 갈수있는 노드가
# 이전에 최단으로 갈 수 없는 노드가 이미 거쳐갔다는 이유로 방문을 못하게 되지 않는지...
# -> 이 부분에 대한 의문은 어느정도 해소 되었다
# -> 백트래킹의 경우 유망하지 않으면 더 탐색을 하지 않을 것이고 유망한 노드를 찾아야하므로
# -> 이전에 거쳤던 경로를 리셋해줘야 한다
# -> 그러나 이건 그것과 달리 최단거리를 찾는 것이라 목적지에 빨리 가는 것을 찾아야 한다
# -> 주변의 가능한 탐색 위치들을 하나씩 모두 큐에 넣고 하나씩 탐색해 나가는 방법이라
# -> 깊이 우선 방식의 백트래킹과는 다른 방법이다

