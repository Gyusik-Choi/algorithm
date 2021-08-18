from collections import deque


def bfs(information):
    visited = [0] * 100001
    visited[information[0]] = 1

    end = information[1]

    deq = deque()
    deq.append([information[0], information[2]])

    while deq:
        info = deq.popleft()
        start, days = info[0], info[1]

        days += 1

        for i in range(3):
            stopover = start
            if i == 0:
                stopover -= 1
            elif i == 1:
                stopover += 1
            else:
                stopover *= 2

            if stopover == end:
                return days

            if 0 <= stopover <= 100000:
                if not visited[stopover]:
                    visited[stopover] = 1
                    deq.append([stopover, days])


N, K = map(int, input().split())
if N == K:
    print(0)
else:
    print(bfs([N, K, 0]))
