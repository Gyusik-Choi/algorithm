import sys


def get_sequence(idx):
    if idx == M:
        for (idx, val) in enumerate(answer):
            sys.stdout.write(str(val) + " ")
        sys.stdout.write("\n")
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


N, M = map(int, sys.stdin.readline().split())
answer = []
selected = [False] * N
get_sequence(0)
