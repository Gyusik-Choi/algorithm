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
    min_num = INF
    u = -1
    for i in range(V):
        if not selected[i] and distance[i] < min_num:
            min_num = distance[i]
            u = i

    selected[u] = True
    for j in adj[u]:
        end = j[0]
        value = j[1]
        if not selected[end] and distance[end] > value + min_num:
            distance[end] = value + min_num
    cnt += 1


print(distance)
print(selected)

# 참고
# https://m.blog.naver.com/PostView.nhn?blogId=ssarang8649&logNo=220992988177&proxyReferer=https:%2F%2Fwww.google.com%2F
# https://coding-insider.tistory.com/entry/Prim-vs-Dijkstra-%ED%94%84%EB%A6%BC-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EB%B9%84%EA%B5%90
