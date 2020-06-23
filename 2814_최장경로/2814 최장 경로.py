# import sys
# sys.stdin = open("input.txt", "r")


def dfs(array, go, stop):
    global longest, visited
    for k in array[go]:
        if k == stop:
            visited[k] = 1
            if sum(visited) >= longest:
                longest = sum(visited)
            return
        if visited[k] != 1:
            visited[k] = 1
            dfs(array, k, stop)
            visited[k] = 0


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    lst = [[] for _ in range(N + 1)]
    longest = 1
    for i in range(M):
        lst[arr[i][0]].append(arr[i][1])
        lst[arr[i][1]].append(arr[i][0])
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j:
                visited = [0] * (N + 1)
                visited[i] = 1
                dfs(lst, i, j)
    print("#{} {}".format(t, longest))
