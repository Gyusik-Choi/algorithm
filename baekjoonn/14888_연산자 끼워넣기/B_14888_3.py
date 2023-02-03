import math


def back_track(idx, start_number, addition, subtraction, multiply, division):
    global max_num, min_num
    if idx == N - 1:
        max_num = max(start_number, max_num)
        min_num = min(start_number, min_num)
        return
    else:
        if addition:
            back_track(idx + 1, start_number + numbers[idx + 1], addition - 1, subtraction, multiply, division)

        if subtraction:
            back_track(idx + 1, start_number - numbers[idx + 1], addition, subtraction - 1, multiply, division)

        if multiply:
            back_track(idx + 1, start_number * numbers[idx + 1], addition, subtraction, multiply - 1, division)

        if division:
            if start_number >= 0:
                back_track(idx + 1, start_number // numbers[idx + 1], addition, subtraction, multiply, division - 1)
            else:
                back_track(idx + 1, math.ceil(start_number / numbers[idx + 1]), addition, subtraction, multiply, division - 1)


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_num = -float('inf')
min_num = float('inf')

start = numbers[0]
back_track(0, start, operators[0], operators[1], operators[2], operators[3])
print(max_num)
print(min_num)
