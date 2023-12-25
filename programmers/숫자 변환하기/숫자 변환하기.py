from collections import deque


def solution(x, y, n):
    def bfs(start, end, add):
        if start == end:
            return 0

        deq = deque([(start, 0)])
        visited = [False] * 1000000
        visited[start] = True

        while deq:
            num, cnt = deq.popleft()

            for i in range(3):
                number = num

                if i == 0:
                    number += add
                elif i == 1:
                    number *= 2
                else:
                    number *= 3

                if number == end:
                    return cnt + 1

                if number < end and not visited[number]:
                    visited[number] = True
                    deq.append((number, cnt + 1))

        return -1

    return bfs(x, y, n)


print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))
print(solution(1, 1000000, 1))
