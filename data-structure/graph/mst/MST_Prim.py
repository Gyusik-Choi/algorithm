# 최소신장트리(프림, 크루스칼 등)과 다익스트라 차이
# 최소신장트리는 모든 노드들을 연결하는 비용을 따진다
# 다익스트라는 두 노드 간의 비용을 따진다

# 입력값
# 7 11
# 0 5 60
# 0 1 32
# 0 2 31
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51
V, E = map(int, input().split())
adj = [[0] * V for _ in range(V)]
for i in range(E):
    s, e, v = map(int, input().split())
    adj[s][e] = v
    adj[e][s] = v

# mst 최소 신장 트리
# 정점 - 1 개의 개수로 정점들을 최소 비용으로 연결

INF = float('inf')
key = [INF] * V
p = [-1] * V
mst = [False] * V
# 시작 정점 0으로 선택
key[0] = 0
sums = 0
cnt = 0
while cnt < V:
    min = INF
    u = -1
    # mst 아니면서 최소 정점 찾음
    for i in range(V):
        if not mst[i] and min > key[i]:
            min = key[i]
            u = i

    sums += min
    mst[u] = True
    # 찾은 최소 정점과 연결된 정점들 중 mst 가 아닌 정점의 가중치값 갱신
    for w in range(len(adj[u])):
        if not mst[w] and key[w] > adj[u][w] > 0:
            key[w] = adj[u][w]
            p[w] = u
    cnt += 1

print(key)
print(p)
print(sums)

# 참고
# https://m.blog.naver.com/PostView.nhn?blogId=ssarang8649&logNo=220992988177&proxyReferer=https:%2F%2Fwww.google.com%2F
# https://coding-insider.tistory.com/entry/Prim-vs-Dijkstra-%ED%94%84%EB%A6%BC-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EB%B9%84%EA%B5%90
