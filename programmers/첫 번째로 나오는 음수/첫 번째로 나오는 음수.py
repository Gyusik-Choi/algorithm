def solution(num_list):
    for idx, num in enumerate(num_list):
        if num < 0:
            return idx
    return -1


print(solution([12, 4, 15, 46, 38, -2, 15]))
print(solution([13, 22, 53, 24, 15, 6]))
