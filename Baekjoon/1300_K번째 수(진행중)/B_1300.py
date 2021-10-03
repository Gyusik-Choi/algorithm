import sys


def binary_search(start, end):
    global answer
    if start > end:
        return

    mid = (start + end) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid // i, N)

    if cnt < K:
        return binary_search(mid + 1, end)
    else:
        answer = mid
        return binary_search(start, mid - 1)


N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

answer = 0
binary_search(1, K)
sys.stdout.write(str(answer))

# 참고
# https://jaimemin.tistory.com/988
#
