def solution(my_string, target):
    m = len(my_string)
    t = len(target)

    if m < t:
        return 0

    for i in range(m - t + 1):
        if my_string[i:i + t] == target:
            return 1
    return 0


print(solution("banana", "ana"))
# print(solution("banana", "wxyz"))
