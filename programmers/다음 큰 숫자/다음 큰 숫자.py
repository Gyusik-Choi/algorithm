def change_to_binary(n: int) -> str:
    return format(n, 'b')


def find_next_number(origin_number: int, next_number: int):
    binary1 = change_to_binary(origin_number)
    binary2 = change_to_binary(next_number)

    if binary1.count('1') == binary2.count('1'):
        return next_number

    return find_next_number(origin_number, next_number + 1)


def solution(n):
    return find_next_number(n, n + 1)


print(solution(78))
print(solution(15))
