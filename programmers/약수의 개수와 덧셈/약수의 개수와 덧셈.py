import math


def get_number_of_divisor(num):
    sqrt = int(math.sqrt(num))
    divisors = []

    for s in range(1, sqrt + 1):
        q = num // s

        if q * s == num:
            divisors.append(s)

            # 약수와 몫이 같은 경우
            # ex> 25의 약수 5, 몫 5
            if q == s:
                continue

            divisors.append(num // s)

    return len(divisors)


def is_odd_number_of_divisor(num):
    return get_number_of_divisor(num) % 2 == 1


def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        if is_odd_number_of_divisor(num):
            answer -= num
        else:
            answer += num

    return answer


print(solution(13, 17))
print(solution(24, 27))
