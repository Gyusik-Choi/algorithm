def consecutive_nums(target, start):
    sums = 0

    for num in range(start, target + 1):
        sums += num

        if sums == target:
            return True

        if sums > target:
            break

    return False


def solution(s):
    answer = 0

    for num in range(1, s + 1):
        if consecutive_nums(s, num):
            answer += 1

    return answer
