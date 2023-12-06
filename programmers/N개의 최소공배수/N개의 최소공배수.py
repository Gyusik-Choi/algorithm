def is_all_divided(numbers, num):
    for n in numbers:
        if num % n:
            return False
    return True


def solution(arr):
    arr = sorted(arr)
    biggest_number = arr[-1]
    left_numbers = arr[:len(arr) - 1]
    cnt = 0

    while True:
        cnt += 1

        if is_all_divided(left_numbers, biggest_number * cnt):
            break

    return biggest_number * cnt


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
