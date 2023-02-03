import sys


def sliding_window():
    start = 0
    end = 0
    min_length = N
    sums = sequences[0]

    while start <= end < N:
        if sums < S:
            end += 1
            if end == N:
                break
            sums += sequences[end]
        else:
            sums -= sequences[start]
            min_length = min(min_length, end - start + 1)
            start += 1

    return min_length


N, S = map(int, sys.stdin.readline().split())
sequences = list(map(int, sys.stdin.readline().split()))
sum_sequences = sum(sequences)
if sum_sequences < S:
    print(0)
elif S == 0:
    print(1)
else:
    print(sliding_window())

# 연속된 수들의 부분합
# 정렬하면 안 된다

# 반례
# 10 10
# 2 3 4 5 6 1 2 3 4 1
# => 2

# 10 10
# 1 1 1 1 1 1 1 1 1 10
# => 1

# 10 0
# 1 1 1 1 1 1 1 1 1 1
# => 1

# 반례
# https://www.acmicpc.net/board/view/46239
# https://www.acmicpc.net/board/view/54090
# https://www.acmicpc.net/board/view/69989
# https://bingorithm.tistory.com/13 (반례 모음 링크)
# 코드
# https://rightbellboy.tistory.com/82
