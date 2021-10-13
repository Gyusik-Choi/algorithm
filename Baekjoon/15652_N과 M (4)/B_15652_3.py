def get_sequence(idx):
    if idx == M:
        print(*answer)
    else:
        for i in range(N):
            if not answer:
                answer.append(i + 1)
                selected[i] = True
                get_sequence(idx + 1)
                answer.pop()
                selected[i] = False
            else:
                if answer[-1] <= i + 1:
                    answer.append(i + 1)
                    selected[i] = True
                    get_sequence(idx + 1)
                    answer.pop()
                    selected[i] = False


N, M = map(int, input().split())
answer = []
selected = [False] * N
get_sequence(0)
