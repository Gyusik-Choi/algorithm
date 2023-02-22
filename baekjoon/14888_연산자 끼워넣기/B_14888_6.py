def calculate(plus, minus, multiply, division, sums, idx):
    global max_sums, min_sums

    if plus:
        calculate(plus - 1, minus, multiply, division, sums + numbers[idx], idx + 1)

    if minus:
        calculate(plus, minus - 1, multiply, division, sums - numbers[idx], idx + 1)

    if multiply:
        calculate(plus, minus, multiply - 1, division, sums * numbers[idx], idx + 1)

    if division:
        if sums < 0:
            sums *= -1
            sums //= numbers[idx]
            sums *= -1
        else:
            sums //= numbers[idx]

        calculate(plus, minus, multiply, division - 1, sums, idx + 1)

    if idx == len(numbers):
        max_sums = max(max_sums, sums)
        min_sums = min(min_sums, sums)


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_sums = -1000000000
min_sums = 1000000000

calculate(operators[0], operators[1], operators[2], operators[3], numbers[0], 1)

print(max_sums)
print(min_sums)
