import sys


def floyd_warshall():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            for k in range(1, n + 1):
                if j == k:
                    continue

                if visited[j][k] > visited[j][i] + visited[i][k]:
                    visited[j][k] = visited[j][i] + visited[i][k]


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

inf = float('inf')
visited = [[inf] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    # 문제의 조건을 유의해야 한다
    # "시작 도시와 도착 도시가 같은 경우는 없다"만 보게 되면 특정 시작 도시와 도착 도시에 대한 거리가 하나만 주어질 것 같지만
    # "시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다." 라는 조건이 아래에 추가로 명시되어 있다
    # 더 먼 거리로 기존의 값이 덮어씌워질 수 있으므로 주의
    if visited[a][b] > c:
        visited[a][b] = c

floyd_warshall()

for m, one_line in enumerate(visited):
    if not m:
        continue
    for n, each_item in enumerate(one_line):
        if not n:
            continue

        if each_item == float('inf'):
            sys.stdout.write(str(0) + " ")
        else:
            sys.stdout.write(str(each_item) + " ")
    sys.stdout.write("\n")
