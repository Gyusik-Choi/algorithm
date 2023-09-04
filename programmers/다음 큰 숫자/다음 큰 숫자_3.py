def find_next_number(origin_count: int, next_number: int):
    if origin_count == change_to_binary(next_number).count('1'):
        return next_number

    return find_next_number(origin_count, next_number + 1)


def change_to_binary(n):
    binary = ''

    while n >= 2:
        binary += str(n % 2)
        n //= 2

    binary += str(n)
    return ''.join(reversed(list(binary)))


def solution(n):
    return find_next_number(change_to_binary(n).count('1'), n + 1)


print(solution(78))
print(solution(15))

# 60
# 30 -> 0
# 15 -> 0
# 7 -> 1
# 3 -> 1
# 1 -> 1
# 1111000

