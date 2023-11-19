def get_reversed_trinary_digit(n):
    str_num = ''

    # while n >= 3:
    #     str_num += str(n % 3)
    #     n //= 3
    #
    # str_num += str(n)

    # 위의 코드를
    # 아래와 같은 방식으로 변경할 수 있다
    while n:
        str_num += str(n % 3)
        n //= 3

    return str_num


def solution(n):
    str_num = get_reversed_trinary_digit(n)
    length = len(str_num)
    num = 0

    for i in range(length):
        idx = length - i - 1
        num += int(str_num[i]) * (3 ** idx)

    return num


print(solution(45))
print(solution(3))
