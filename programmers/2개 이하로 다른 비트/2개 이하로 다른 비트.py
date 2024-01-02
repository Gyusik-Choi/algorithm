def solution(numbers):
    def get_bigger_number(number):
        return int(get_bigger_binary_number(number), 2)

    def get_bigger_binary_number(number):
        number = '0' + bin(number)[2:]
        idx = number.rfind('0')
        number = list(number)
        number[idx], number[idx + 1] = '1', '0'
        return ''.join(number)

    return list(map(lambda x: x + 1 if not x % 2 else get_bigger_number(x), numbers))


print(solution([2, 7]))
print(solution([7]))
