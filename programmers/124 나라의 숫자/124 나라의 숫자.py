def solution(n):
    num = ''
    while n:
        remainder = n % 3
        n //= 3
        if not remainder:
            num += '4'
            n -= 1
        else:
            num += str(remainder)

    return num[::-1]


# 참고
# https://hoons-dev.tistory.com/67
# https://latte-is-horse.tistory.com/127
