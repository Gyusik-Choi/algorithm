# 신장트리: 각 정점들을 싸이클 없이 모두 연결하는 그래프
# 최소신장트리: 최소 비용으로 각 정점들을 싸이클 없이 모두 연결하는 그래프
# 정점의 수 = 간선의 수 + 1

# MST PRIM 알고리즘은 정점 중심
# 각 정점별 가중치를 무한대로 설정하고
# 임의의 정점을 시작 위치로 정한 뒤에
# 해당 정점과 인접한 정점들 간의 가중치를 기존의 설정한 가중치(무한대)와 비교하여 더 작은 값으로 변경

V, E = map(int, input().split())
adj = {i: [] for i in range(V)}
for i in range(E):
    s, e, v = map(int, input().split())
    # 무방향이기 때문에 출발점과 도착점이 둘 다 될 수 있다
    adj[s].append([e, v])
    adj[e].append([s, v])

INF = float('inf')
# 가중치(비용)
key = [INF] * V
# 부모 정점
p = [-1] * V
# MST 여부(싸이클 생기지 않도록 체크하는 기능)
mst = [False] * V
# 임의의 정점을 시작 위치로 정하는데 여기서 0번 인덱스를 시장 정점으로 선택
# key 를 돌면서 최소 가중치 지점을 찾을 것이라 0번 인덱스의 값을 0으로 하면서 0번이 선택되도록 한다
key[0] = 0

# 최소비용
sums = 0
cnt = 0
while cnt < V:
    # 최소 가중치 값
    min_key = INF
    # 최소 가중치 인덱스
    min_idx = -1
    # 최소 가중치 갖는 정점 찾기
    for i in range(V):
        if not mst[i] and min_key > key[i]:
            min_key = key[i]
            min_idx = i
    print(min_idx)
    # 최소 가중치 정점을 정점으로 선택했음을 체크
    mst[min_idx] = True
    # 비용 추가
    sums += min_key
    # 최소 가중치 정점과 연결된 정점들 중에서 기존의 가중치 값보다 작은 가중치 값을 가진 경우 더 작은 값으로 바꿔준다(비용 업데이트)
    # 부모 정점 표시
    for end, value in adj[min_idx]:
        if not mst[end] and key[end] > value:
            key[end] = value
            p[end] = min_idx
    cnt += 1

print(key)
print(p)
print(mst)
print(sums)
print(cnt)

# 참고
# https://blog.naver.com/ssarang8649/220992988177
