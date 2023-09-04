def find_next_number(origin_count: int, next_number: int):
    if origin_count == bin(next_number).count('1'):
        return next_number

    return find_next_number(origin_count, next_number + 1)


def solution(n):
    return find_next_number(bin(n).count('1'), n + 1)


print(solution(78))
print(solution(15))
