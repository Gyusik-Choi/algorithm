def dfs(start):
    global is_cycle

    for end in edges[start]:
        if not visited[end]:
            visited[end] = 1
            dfs(end)
        else:
            # 사이클
            # stack 에 담기지 않았는데 end 를 방문처리 한 이후에 다시 만나게 된 상황
            # 재귀를 수행하는 과정에서 end 를 다시 만나게 된 것
            if end not in stack:
                is_cycle = True
                return
    stack.append(start)


# 정점, 간선 갯수
v, e = map(int, input().split())
edges = {i: [] for i in range(1, v + 1)}

for _ in range(e):
    s, e = map(int, input().split())
    edges[s].append(e)

visited = [0] * (v + 1)
stack = []
is_cycle = False

for i in range(1, v + 1):
    if not visited[i] and not is_cycle:
        visited[i] = 1
        dfs(i)

if not is_cycle:
    while stack:
        print(stack.pop(), end=" ")
    print()
else:
    print('사이클')

# 사이클 X
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

# 사이클 O
# 7 9
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
# 7 4

# 이것이 코딩 테스드다 (나동빈)
# https://velog.io/@jeongmin/%EC%9C%84%EC%83%81-%EC%A0%95%EB%A0%ACtopological-sorting
