def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    sorted_numbers_str = sorted(numbers_str, key=lambda num: num * 3, reverse=True)
    return str(int(''.join(sorted_numbers_str)))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
