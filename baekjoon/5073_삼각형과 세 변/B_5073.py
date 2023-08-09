import sys


def is_longer_than_max(a, b, c):
    arr = [a, b, c]
    max_num = max(arr)
    arr.remove(max_num)
    return max_num < sum(arr)


def check_triangle():
    answer = ''

    while True:
        a, b, c = map(int, sys.stdin.readline().split())

        if a == b == c == 0:
            break

        if not is_longer_than_max(a, b, c):
            answer += 'Invalid\n'
            continue

        if a == b == c:
            answer += 'Equilateral\n'
            continue

        if len(list({a, b, c})) == 2:
            answer += 'Isosceles\n'
            continue

        answer += 'Scalene\n'

    answer = answer.rstrip('\n')
    sys.stdout.write(answer)


check_triangle()
