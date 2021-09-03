import heapq
import sys


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
adj = {i: [] for i in range(1, V + 1)}
for _ in range(E):
    s, e, v = map(int, sys.stdin.readline().split())
    adj[s].append([e, v])

INF = float('inf')
selected = [False] * (V + 1)
distance = [INF] * (V + 1)
distance[K] = 0

h = []
heapq.heappush(h, (0, K))

while h:
    key, start = heapq.heappop(h)
    if not adj[start]:
        continue

    selected[start] = True
    for end, value in adj[start]:
        if distance[end] > distance[start] + value and not selected[end]:
            distance[end] = distance[start] + value
            heapq.heappush(h, (distance[end], end))

for i in range(1, V + 1):
    if distance[i] != INF:
        sys.stdout.write(str(distance[i]) + "\n")
    else:
        sys.stdout.write(str("INF") + "\n")

# 시간초과 때문에 우선순위 큐를 도입했는데
# 1번부터 시작하려고 하니 우선순위 큐의 최소값부터 나오는 방식 때문에
# 어떻게 1번부터 시작할 수 있도록 할지 모르겠음
# => 풀이방법을 제대로 이해하지 못해서 위와 같은 고민을 했다
# => 우선순위 큐에 넣어야할 값은 가중치(v)가 아니다
# => 시작점을 기준으로 계산해나가는 distance 배열의 값이다
# => 그래야 가장 거리가 가까운 정점을 우선순위 큐에서 뽑을 수 있다
# => 입력받은 가중치(v)는 특정 간선의 가중치라 특정 정점까지 오는 경로값이 아니다
# => K부터 출발하기 위해서 K의 distance 값을 0으로 설정했고 이를 우선순위 큐에 넣는다
