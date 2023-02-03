import sys


def get_sequence(idx):
    if idx == M:
        sys.stdout.write(' '.join(answer) + "\n")
    else:
        for i in range(N):
            if visited[i] is False:
                visited[i] = True
                answer.append(str(i + 1))
                get_sequence(idx + 1)
                visited[i] = False
                answer.pop()


N, M = map(int, sys.stdin.readline().split())
answer = []
visited = [False] * N

get_sequence(0)
