import sys
import heapq


def mst_prim():
    mst = [False] * N
    heap = []
    # 비용, 출발점
    # 비용은 출발점만 있고 도착점이 없으므로 0 이다
    # 출발점은 임의로 0 설정
    heapq.heappush(heap, (0, 0))
    min_cost = 0
    cnt = 0

    while heap:
        cost, start = heapq.heappop(heap)

        if mst[start]:
            continue

        mst[start] = True
        min_cost += cost

        for end_cost, end in total_axis[start]:
            if not mst[end]:
                heapq.heappush(heap, (end_cost, end))

        cnt += 1
        # kruskal 과 다르게 N - 1 이 아니라 N 임에 주의
        if cnt == N:
            break

    return min_cost


N = int(sys.stdin.readline())

x_axis = []
y_axis = []
z_axis = []

for i in range(N):
    X, Y, Z = map(int, sys.stdin.readline().split())
    x_axis.append([X, i])
    y_axis.append([Y, i])
    z_axis.append([Z, i])

x_axis.sort()
y_axis.sort()
z_axis.sort()

total_axis = {i: [] for i in range(N)}
# heap = []

for i in range(N - 1):
    # 간선 중심인 크루스칼과 구분해야 한다
    # 크루스칼은 비용이 가장 작은 간선부터 선택해 나가야 하므로
    # total_axis 를 정렬 했지만
    # 정점 중심인 프림은 여기서 정렬 하지 않는다
    # 또한 프림은 i 뿐만 아니라 i + 1 에 대한 정보도 넣어줘야 한다
    # 간선 중심이 아니라 정점 중심이므로 i, i + 1 중에 어떤 점을 출발점으로 삼을지 모르기 때문이다
    total_axis[x_axis[i][1]].append([x_axis[i + 1][0] - x_axis[i][0], x_axis[i + 1][1]])
    total_axis[x_axis[i + 1][1]].append([x_axis[i + 1][0] - x_axis[i][0], x_axis[i][1]])
    total_axis[y_axis[i][1]].append([y_axis[i + 1][0] - y_axis[i][0], y_axis[i + 1][1]])
    total_axis[y_axis[i + 1][1]].append([y_axis[i + 1][0] - y_axis[i][0], y_axis[i][1]])
    total_axis[z_axis[i][1]].append([z_axis[i + 1][0] - z_axis[i][0], z_axis[i + 1][1]])
    total_axis[z_axis[i + 1][1]].append([z_axis[i + 1][0] - z_axis[i][0], z_axis[i][1]])

    # heapq.heappush(heap, (x_axis[i + 1][0] - x_axis[i][0], x_axis[i][1], x_axis[i + 1][1]))
    # heapq.heappush(heap, (y_axis[i + 1][0] - y_axis[i][0], y_axis[i][1], y_axis[i + 1][1]))
    # heapq.heappush(heap, (z_axis[i + 1][0] - z_axis[i][0], z_axis[i][1], z_axis[i + 1][1]))

print(mst_prim())

# total_axis 에 좌표 기준으로 정렬된 정점들 간의 비용 기준으로 정렬
#
# prim 으로 할 때 바로 heap 에 넣는건 왜 안될까?
# prim 구현 연습할 때 heap 에 바로 넣지 않는 것과 같은 원리라 생각한다.
# 모든 정보를 heap 에 넣는게 아니라 임의의 출발점을 정한 후에 그 출발점과 연결된 정점들만 heap 에 넣고
# 그 중 가장 가까운 거리의 정점을 꺼내서 진행하는 방식이다.
#
# 이 문제에서 임의의 출발점을 잡는게 맞는지 의문이다.
# x, y, z 를 각각 좌표 값을 기준으로 정렬 했으므로 정렬한 좌표 값들의 가장 첫번째 인덱스부터 출발해야 한다.
# 그러므로 임의의 출발점을 0으로 잡으면 될 것 같다.
#
# 그러면 다시 질문으로 돌아와 보자. 왜 안될까? 출발점에서 하나씩 연결될 수 없다.
# prim 은 하나씩 연결해 나가야 하는데 이 문제는 힙에서 꺼내면 출발점과 도착점이 같이 있다.
# 일단 mst 에 무엇을 체크해야 할지도 모호하다. 만약에 mst 에 출발점만 체크하면 그 출발점으로부터 연결되는걸 찾을 수 없다.
# 1, 2 가 나와서 1을 체크하고 다음에 1, 3이 나올 수 있다. 이러면 2, 3은 그냥 버려진다.
# 1과 연결될 점을 찾아야 하는데 연결될 점을 찾지 못하고 끝나 버린다.
#
# 다음 힙에서 꺼낸게 출발점으로 부터 다른 도착점이 나오는게 아니라 임의의 출발점, 도착점이 나온다.
# 출앞서 나온 출발점과 연결이 아니라 별개의 연결선이다.
#
# 이 문제를 프림으로 다시 풀이 하면서 헤맸던 주요 원인은 크루스칼이 간선 중심, 프림이 정점 중심 이라는 것을 간과한 점이다
