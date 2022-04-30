def recursion(cnt, sums, plus, minus, multiply, division):
    global max_sums, min_sums
    if cnt == N - 1:
        max_sums = max(max_sums, sums)
        min_sums = min(min_sums, sums)
    else:
        if plus:
            recursion(cnt + 1, sums + numbers[cnt + 1], plus - 1, minus, multiply, division)

        if minus:
            recursion(cnt + 1, sums - numbers[cnt + 1], plus, minus - 1, multiply, division)

        if multiply:
            recursion(cnt + 1, sums * numbers[cnt + 1], plus, minus, multiply - 1, division)

        if division:
            if sums < 0:
                recursion(cnt + 1, sums * -1 // numbers[cnt + 1] * -1, plus, minus, multiply, division - 1)
            else:
                recursion(cnt + 1, sums // numbers[cnt + 1], plus, minus, multiply, division - 1)


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_sums = -float('inf')
min_sums = float('inf')

recursion(0, numbers[0], operators[0], operators[1], operators[2], operators[3])
print(max_sums)
print(min_sums)
