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
            if i == 0:
                start -= 1
            elif i == 1:
                start += 1
            else:
                start *= 2

            if start == end:
                return days

            if 0 <= start <= 100000:
                if not visited[start]:
                    visited[start] = 1
                    deq.append([start, days])


N, K = map(int, input().split())
if N == K:
    print(0)
else:
    print(bfs([N, K, 0]))

# 반례 99999 100000
# 틀릴 수 밖에 없었다
# start 가 초기화되지 못했다
