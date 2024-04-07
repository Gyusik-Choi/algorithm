def solution(num_list):
    return [len(list(filter(lambda x: x % 2 == 0, num_list))),
            len(list(filter(lambda x: x % 2 == 1, num_list)))]


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))
