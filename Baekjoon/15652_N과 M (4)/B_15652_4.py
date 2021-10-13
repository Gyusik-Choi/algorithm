def get_sequence(val, idx):
    if idx == M:
        print(*answer)
    else:
        for i in range(val, N + 1):
            answer[idx] = i
            get_sequence(i, idx + 1)


N, M = map(int, input().split())
answer = [0] * M
selected = [False] * N
get_sequence(1, 0)

# 참고
# https://st-lab.tistory.com/117
