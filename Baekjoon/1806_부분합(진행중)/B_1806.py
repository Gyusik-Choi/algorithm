import sys


def get_direction(sums, start, end):
    if sums - sequences[start] >= S and sums - sequences[end] >= S:
        if sequences[start] > sequences[end]:
            return 1
        return 0
    elif sums - sequences[start] >= S:
        return 0
    elif sums - sequences[end] >= S:
        return 1
    else:
        return -1


def two_pointers(sums, start, end):
    answer = N

    while start <= end:
        direction = get_direction(sums, start, end)
        if direction == -1:
            # 이 부분 수정 필요
            # 정렬이 된 상태라 아니라서 더 진행할 수 있으면 추가적으로 살펴봐야한다
            return answer

        if not direction:
            sums -= sequences[start]
            answer -= 1
            start += 1
        else:
            sums -= sequences[end]
            answer -= 1
            end -= 1

    if answer == 0:
        return 1
    return answer


N, S = map(int, sys.stdin.readline().split())
sequences = list(map(int, sys.stdin.readline().split()))
sum_sequences = sum(sequences)
if sum_sequences < S:
    print(0)
else:
    minimum_length = two_pointers(sum_sequences, 0, N - 1)
    print(minimum_length)

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

# https://www.acmicpc.net/board/view/46239
# https://www.acmicpc.net/board/view/54090
# https://www.acmicpc.net/board/view/69989
