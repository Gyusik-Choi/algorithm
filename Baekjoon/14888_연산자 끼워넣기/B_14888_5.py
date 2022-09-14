def calculate(operator_combination):
    sums = numbers[0]

    for idx, operator in enumerate(operator_combination):
        # +
        if operator == 0:
            sums += numbers[idx + 1]
        # -
        elif operator == 1:
            sums -= numbers[idx + 1]
        # *
        elif operator == 2:
            sums *= numbers[idx + 1]
        # //
        else:
            if sums >= 0:
                sums //= numbers[idx + 1]
            else:
                sums *= -1
                sums //= numbers[idx + 1]
                sums *= -1

    return sums


def combination(operator_info, temp_operators):
    global max_sums, min_sums

    if len(temp_operators) == len(numbers) - 1:
        sums = calculate(temp_operators)

        if sums > max_sums:
            max_sums = sums

        if sums < min_sums:
            min_sums = sums

        return

    for idx, operator in enumerate(operator_info):
        if operator_info[idx] > 0:
            operator_info[idx] -= 1
            temp_operators.append(idx)
            combination(operator_info, temp_operators)
            operator_info[idx] += 1
            temp_operators.pop()


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_sums = -1000000000
min_sums = 1000000000

combination(operators, [])

print(max_sums)
print(min_sums)
