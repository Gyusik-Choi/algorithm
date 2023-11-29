def dfs(computer_map, visited, start):
    if visited[start]:
        return

    visited[start] = True

    for end in computer_map[start]:
        dfs(computer_map, visited, end)


def get_network_cnt(n, computer_map):
    visited = [False] * n
    cnt = 0

    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(computer_map, visited, i)

    return cnt


def solution(n, computers):
    adj = dict()

    for i, computer in enumerate(computers):
        adj[i] = []

        for j, c in enumerate(computer):
            if i != j and c:
                adj[i].append(j)

    return get_network_cnt(n, adj)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
