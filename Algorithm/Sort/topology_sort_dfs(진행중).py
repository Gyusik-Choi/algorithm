def dfs(start):
    for end in edges[start]:
        if not visited[end]:
            visited[end] = 1
            dfs(end)
    stack.append(start)


# 정점, 간선 갯수
v, e = map(int, input().split())
edges = {i: [] for i in range(1, v + 1)}

for _ in range(e):
    s, e = map(int, input().split())
    edges[s].append(e)

visited = [0] * (v + 1)
stack = []

for i in range(1, v + 1):
    if not visited[i]:
        visited[i] = 1
        dfs(i)

while stack:
    print(stack.pop(), end=" ")
print()

# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
# => 1 5 2 6 3 4 7

# 이것이 코딩 테스드다 (나동빈)
# https://velog.io/@jeongmin/%EC%9C%84%EC%83%81-%EC%A0%95%EB%A0%ACtopological-sorting
