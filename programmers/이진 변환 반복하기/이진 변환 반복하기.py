import re


def get_binary_number(s):
    binary_number = ''

    while s:
        binary_number = str(s % 2) + binary_number
        s //= 2

    return binary_number


def filter_zero(s):
    return re.findall('1', s)


def solution(s):
    cnt = 0
    zero_cnt = 0

    while s != "1":
        filtered_number = filter_zero(s)
        binary_number = get_binary_number(int(len(filtered_number)))

        cnt += 1
        zero_cnt += len(s) - len(filtered_number)

        s = binary_number

    return [cnt, zero_cnt]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
