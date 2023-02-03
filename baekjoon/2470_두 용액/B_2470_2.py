import sys


def two_pointers(start, end):
    min_sums = float('inf')
    min_solutions = []

    while start < end:
        start_value = sorted_solutions[start]
        end_value = sorted_solutions[end]
        sums = start_value + end_value

        if sums == 0:
            min_solutions = [start_value, end_value]
            return min_solutions

        if min_sums > abs(sums):
            min_sums = abs(sums)
            min_solutions = [start_value, end_value]

        if sums < 0:
            start += 1
        else:
            end -= 1

    return min_solutions


N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
sorted_solutions = sorted(solutions)

answer = two_pointers(0, N - 1)
answer.sort()
for item in answer:
    sys.stdout.write(str(item) + " ")

# 반례
# 5
# -5 -4 -3 -2 -1
# => -2 -1

# 6
# -99 -60 3 7 61 130
# => -60 61

# 참고
# https://www.acmicpc.net/board/view/53660
# https://ansohxxn.github.io/boj/2470/#-%EB%82%9C%EC%9D%B4%EB%8F%84
