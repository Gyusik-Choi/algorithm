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
adj = {i: [] for i in range(V)}
for i in range(E):
    s, e, v = map(int, input().split())
    adj[s].append([e, v])
    adj[e].append([s, v])

INF = float('inf')
distance = [INF] * V
selected = [False] * V

distance[0] = 0
cnt = 0
while cnt < V:
    min_value = INF
    min_vertex = -1

    # 가중치 가장 작은 노드 찾기
    for j in range(V):
        if not selected[j] and min_value > distance[j]:
            min_value = distance[j]
            min_vertex = j

    # 인접 노드들의 최소거리 업데이트
    for end, value in adj[min_vertex]:
        if not selected[end] and distance[end] > distance[min_vertex] + value:
            distance[end] = distance[min_vertex] + value

    selected[min_vertex] = True
    cnt += 1

print(distance)

# 참고
# https://m.blog.naver.com/PostView.nhn?blogId=ssarang8649&logNo=220992988177&proxyReferer=https:%2F%2Fwww.google.com%2F
# https://coding-insider.tistory.com/entry/Prim-vs-Dijkstra-%ED%94%84%EB%A6%BC-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EB%B9%84%EA%B5%90
