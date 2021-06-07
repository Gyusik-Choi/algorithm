from collections import deque


def bfs(n):
    deq = deque()
    deq.append([n, 0])
    while deq:
        point, time = deq.popleft()
        for i in range(3):
            older_sister = point

            if i == 0:
                older_sister -= 1
            elif i == 1:
                older_sister += 1
            else:
                older_sister *= 2

            if older_sister == K:
                return time + 1
            else:
                if 0 <= older_sister <= 100000:
                    if visited[older_sister] == 0:
                        visited[older_sister] = 1
                        deq.append([older_sister, time + 1])


N, K = map(int, input().split())
visited = [0] * 100001
visited[N] = 1
visited[K] = 1

if N == K:
    print(0)
elif N > K:
    print(N - K)
else:
    ans = bfs(N)
    print(ans)
