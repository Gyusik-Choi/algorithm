def dfs(virus):
    global cnt
    stack = [virus]
    while stack:
        tmp = stack.pop()
        for node in arr[tmp]:
            if node not in stack and not visited[node]:
                stack.append(node)
        visited[tmp] = 1
        cnt += 1


N = int(input())
link = int(input())
arr = {i: [] for i in range(1, N + 1)}
for i in range(link):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (N + 1)
cnt = -1
dfs(1)
print(cnt)
