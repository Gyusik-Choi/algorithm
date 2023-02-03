def get_sequence(idx):
    if idx == M:
        print(*answer)
    else:
        for i in range(N):
            answer.append(i + 1)
            get_sequence(idx + 1)
            answer.pop()


N, M = map(int, input().split())
answer = []
get_sequence(0)
