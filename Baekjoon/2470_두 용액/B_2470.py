# 반례
# 5
# -5 -4 -3 -2 -1
# => -2 -1

# 6
# -99 -60 3 7 61 130
# => -60 61

import sys


def where_to_go(start, end):
    start_plus = sorted_solutions[start + 1] + sorted_solutions[end]
    minus_end = sorted_solutions[start] + sorted_solutions[end - 1]

    if abs(start_plus) < abs(minus_end):
        return True
    return False


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

        result = where_to_go(start, end)
        if result:
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
