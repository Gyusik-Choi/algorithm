class Operator:
    def __init__(self, cnt, limit, addition, subtraction, multiply, division, sums):
        self.cnt = cnt
        self.limit = limit
        self.addition = addition
        self.subtraction = subtraction
        self.multiply = multiply
        self.division = division
        self.sums = sums


def get_max_and_min_value(operator: Operator):
    global max_value, min_value

    if operator.cnt == operator.limit:
        max_value = max(max_value, operator.sums)
        min_value = min(min_value, operator.sums)
        return

    if operator.addition:
        get_max_and_min_value(
            Operator(
                operator.cnt + 1,
                operator.limit,
                operator.addition - 1,
                operator.subtraction,
                operator.multiply,
                operator.division,
                operator.sums + numbers[operator.cnt]
            )
        )

    if operator.subtraction:
        get_max_and_min_value(
            Operator(
                operator.cnt + 1,
                operator.limit,
                operator.addition,
                operator.subtraction - 1,
                operator.multiply,
                operator.division,
                operator.sums - numbers[operator.cnt]
            )
        )

    if operator.multiply:
        get_max_and_min_value(
            Operator(
                operator.cnt + 1,
                operator.limit,
                operator.addition,
                operator.subtraction,
                operator.multiply - 1,
                operator.division,
                operator.sums * numbers[operator.cnt]
            )
        )

    if operator.division:
        get_max_and_min_value(
            Operator(
                operator.cnt + 1,
                operator.limit,
                operator.addition,
                operator.subtraction,
                operator.multiply,
                operator.division - 1,
                operator.sums // numbers[operator.cnt]
                    if operator.sums >= 0
                    else ((operator.sums * -1) // numbers[operator.cnt]) * -1
            )
        )


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_value = -1000000000
min_value = 1000000000
get_max_and_min_value(Operator(1, N, operators[0], operators[1], operators[2], operators[3], numbers[0]))
print(max_value)
print(min_value)
