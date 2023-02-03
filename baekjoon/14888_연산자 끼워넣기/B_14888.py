import math


def cal(idx, sums, p, s, m, d):
    global max_sums, min_sums
    if idx == N - 1:
        max_sums = max(sums, max_sums)
        min_sums = min(sums, min_sums)
        return
    else:
        if p:
            cal(idx + 1, sums + nums[idx + 1], p - 1, s, m, d)
        if s:
            cal(idx + 1, sums - nums[idx + 1], p, s - 1, m, d)
        if m:
            cal(idx + 1, sums * nums[idx + 1], p, s, m - 1, d)
        if d:
            if sums < 0:
                cal(idx + 1, math.ceil(sums / nums[idx + 1]), p, s, m, d - 1)
            else:
                cal(idx + 1, sums // nums[idx + 1], p, s, m, d - 1)


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_sums = -float('inf')
min_sums = float('inf')

plus = operators[0]
subtraction = operators[1]
multiply = operators[2]
division = operators[3]

cal(0, nums[0], plus, subtraction, multiply, division)
print(max_sums)
print(min_sums)
