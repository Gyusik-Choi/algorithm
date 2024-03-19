def solution(num_list):
    reversed_list = []
    for i in range(len(num_list) - 1, -1, -1):
        reversed_list.append(num_list[i])
    return reversed_list


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))
