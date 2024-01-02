def solution(numbers):
    def get_bigger_number(number):
        return get_decimal_number(get_bigger_binary_number(number))

    def get_decimal_number(binary_number):
        binary_number = list(binary_number[::-1])
        decimal_number = 0
        for i in range(len(binary_number)):
            decimal_number += int(binary_number[i]) * (2 ** i)
        return decimal_number

    def get_bigger_binary_number(number):
        number = '0' + get_binary_number(number)
        idx = number.rfind('0')
        number = list(number)
        number[idx], number[idx + 1] = '1', '0'
        return ''.join(number)

    def get_binary_number(number):
        binary_number = ''

        while number:
            binary_number += str(number % 2)
            number //= 2

        return binary_number[::-1]

    return list(map(lambda x: x + 1 if not x % 2 else get_bigger_number(x), numbers))


print(solution([2, 7]))
print(solution([7]))
