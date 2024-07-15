def solution(my_string, target):
    return int(target in my_string)


print(solution("banana", "ana"))
print(solution("banana", "wxyz"))
