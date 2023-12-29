def solution(n, computers):
    def dfs(start):
        for end in edges[start]:
            if not visited[end]:
                visited[end] = True
                dfs(end)

    edges = {i: [] for i in range(n)}
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i != j and computers[i][j]:
                edges[i].append(j)

    visited = [False] * n
    cnt = 0

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i)

    return cnt


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
